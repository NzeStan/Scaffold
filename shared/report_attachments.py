"""
Report attachments - PDFs dropped into <generator>/attachments/ are placed inside the
report, after the last calculation sheet and before the conclusion.

How it works
  1. collect_attachments()  lists the PDFs (filename order) and counts their pages.
  2. The report template reserves one A4 portrait page per attachment page, each with a
     heading ("ATTACHMENT 1 - TITLE") - so the browser numbers those pages, and the table
     of contents / bookmarks / "Page X of Y" footer all include them.
  3. place_attachments() then draws each attachment page (as vector content, so text stays
     sharp and searchable) onto its reserved page, scaled to fit the page area below the
     heading.

The reserved-page geometry below must match the .attachment-* rules in report.html.
"""
import re
from pathlib import Path

MM = 72.0 / 25.4

# Reserved-page geometry (mm): A4 portrait, report page margins 12mm sides / 12mm top,
# then a 16mm heading band, then the attachment area.
MARGIN_LEFT_MM = 12.0
MARGIN_TOP_MM = 12.0
HEAD_MM = 16.0
SLOT_WIDTH_MM = 186.0     # 210 - 2 x 12
SLOT_HEIGHT_MM = 249.0
SLOT_INSET_MM = 1.0       # keep the placed page off the very edge of the area


def _natural_key(path):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', path.name)]


def _title_from_filename(stem):
    """'02_Hoist-Data_Sheet' -> 'Hoist Data Sheet' (numeric ordering prefix dropped)."""
    title = re.sub(r'^\s*\d+[\s._-]*', '', stem)
    title = re.sub(r'[_\-]+', ' ', title)
    title = re.sub(r'\s+', ' ', title).strip()
    return title or stem


def collect_attachments(folder):
    """PDFs in `folder`, in filename order -> [{'index','title','anchor','path','pages'}]."""
    folder = Path(folder)
    if not folder.is_dir():
        return []
    try:
        from pypdf import PdfReader
    except ImportError:
        if any(folder.glob('*.pdf')):
            print("  [WARN] Install pypdf to include attachment PDFs: pip install pypdf")
        return []

    attachments = []
    for path in sorted(folder.glob('*.pdf'), key=_natural_key):
        try:
            reader = PdfReader(str(path), strict=False)
            if reader.is_encrypted and not reader.decrypt(''):
                print(f"  [WARN] Attachment skipped (password protected): {path.name}")
                continue
            pages = len(reader.pages)
        except Exception as exc:
            print(f"  [WARN] Attachment skipped (unreadable): {path.name} - {exc}")
            continue
        if pages < 1:
            print(f"  [WARN] Attachment skipped (no pages): {path.name}")
            continue
        index = len(attachments) + 1
        attachments.append({
            'index': index,
            'title': _title_from_filename(path.stem),
            'anchor': f'attachment-{index}',
            'path': path,
            'pages': pages,
        })
    return attachments


def place_attachments(pdf_path, attachments):
    """Draw every attachment page onto its reserved page in the rendered report PDF."""
    if not attachments:
        return False
    try:
        from pypdf import PdfReader, PdfWriter, Transformation
    except ImportError:
        print("  [WARN] Install pypdf to include attachment PDFs: pip install pypdf")
        return False

    pdf_path = Path(pdf_path)
    tmp_pdf = pdf_path.with_name(f"{pdf_path.stem}_tmp_attachments.pdf")
    try:
        base = PdfReader(str(pdf_path), strict=False)
        first_pages = {}
        for name, dest in getattr(base, 'named_destinations', {}).items():
            key = str(name).lstrip('/')
            if key.startswith('attachment-'):
                first_pages[key] = base.get_destination_page_number(dest)

        # Every attachment must sit on the pages reserved for it, back to back
        expected_next = None
        for att in attachments:
            first = first_pages.get(att['anchor'])
            if first is None or (expected_next is not None and first != expected_next):
                print("  [WARN] Attachments not placed: reserved pages were not found where "
                      f"expected in the PDF ({att['anchor']}).")
                return False
            expected_next = first + att['pages']
        if expected_next > len(base.pages):
            print("  [WARN] Attachments not placed: reserved pages run past the end of the PDF.")
            return False

        writer = PdfWriter(clone_from=base)
        placed = 0
        for att in attachments:
            src_reader = PdfReader(str(att['path']), strict=False)
            if src_reader.is_encrypted:
                src_reader.decrypt('')
            first = first_pages[att['anchor']]
            for k in range(att['pages']):
                target = writer.pages[first + k]
                src = src_reader.pages[k]
                src.transfer_rotation_to_content()

                box = src.cropbox
                src_w, src_h = float(box.width), float(box.height)
                if src_w <= 0 or src_h <= 0:
                    continue
                area_w = (SLOT_WIDTH_MM - 2 * SLOT_INSET_MM) * MM
                area_h = (SLOT_HEIGHT_MM - 2 * SLOT_INSET_MM) * MM
                scale = min(area_w / src_w, area_h / src_h)

                page_h = float(target.mediabox.height)
                area_left = (MARGIN_LEFT_MM + SLOT_INSET_MM) * MM
                area_top = page_h - (MARGIN_TOP_MM + HEAD_MM + SLOT_INSET_MM) * MM
                # centred horizontally, top-aligned under the heading
                tx = area_left + (area_w - src_w * scale) / 2 - float(box.left) * scale
                ty = area_top - src_h * scale - float(box.bottom) * scale
                target.merge_transformed_page(src, Transformation().scale(scale, scale).translate(tx, ty))
                placed += 1

        with open(tmp_pdf, 'wb') as fout:
            writer.write(fout)
        tmp_pdf.replace(pdf_path)
        print(f"  PDF   ->  placed {len(attachments)} attachment PDF(s), {placed} page(s), before the conclusion")
        return True
    except Exception as exc:
        print(f"  [WARN] Could not place attachments: {exc}")
        try:
            tmp_pdf.unlink(missing_ok=True)
        except Exception:
            pass
        return False
