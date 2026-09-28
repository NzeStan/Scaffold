ATTACHMENTS FOLDER
==================
Drop PDF files here and they are placed inside the report, after the last calculation
sheet and before the Conclusion. Each PDF page gets its own report page with a heading
("ATTACHMENT 1 - TITLE"), the normal "Page X of Y" numbering, and an entry in the
table of contents and PDF bookmarks.

NAMING
  Files are placed in filename order, so start the name with a number:
      01_Hoist-Datasheet.pdf
      02_Manufacturer-Certificate.pdf
  The heading and table-of-contents entry come from the rest of the filename
  (number removed; dashes and underscores become spaces):
      01_Hoist-Datasheet.pdf  ->  "Attachment 1 - Hoist Datasheet"

PAGES
  A PDF can have any number of pages - every page is included, in order, and the heading
  shows (PAGE 2 OF 3) etc. Pages are scaled to fit the A4 portrait report page (landscape
  pages are scaled down to fit, not rotated).

NOTES
  - Password-protected or unreadable PDFs are skipped with a warning.
  - Links inside an attached PDF do not carry over.
  - An empty (or missing) attachments folder changes nothing in the report.
