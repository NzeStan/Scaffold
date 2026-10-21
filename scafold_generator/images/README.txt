IMAGES FOLDER - NAMING GUIDE
=============================
Drop STAAD.Pro screenshots here with exactly these filenames.
Supported extensions: .png, .jpg, .jpeg

3D MODEL:
  3d_model.png              -> 3D isometric view. Generated automatically when
                               AUTO_RENDER_3D_MODEL is "yes" in project_info.txt
                               (overwritten on every run), otherwise drop your own.

LOAD DIAGRAMS:
  load_platform_live.png    -> Platform live load diagram (LL)
  load_handrail_x.png       -> Handrail load X-axis diagram (HLX), when applicable
  load_handrail_z.png       -> Handrail load Z-axis diagram (HLZ), when applicable
  load_wind_x.png           -> Wind load X-axis diagram (only if the model has wind loads)
  load_wind_z.png           -> Wind load Z-axis diagram (only if the model has wind loads)

  One diagram is needed per LL / handrail load case. The first case uses the names above;
  every further case (TITLE LL-1, LL-2, etc.) adds a numbered file:
  load_platform_live_1.png, load_platform_live_2.png ...   -> LL-1, LL-2 ...
  load_handrail_x_1.png,    load_handrail_x_2.png ...      -> HLX-1, HLX-2 ...
  load_handrail_z_1.png,    load_handrail_z_2.png ...      -> HLZ-1, HLZ-2 ...
  The report shows as many diagrams as the model has cases (captioned "Live Load (LL)-1"
  etc). Wind stays a single diagram each, since wind is applied once for the whole model.

WIND CALCULATION:
  No extra image is required. Wind is computed from the .std file.

CONNECTION STABILITY CHECK:
  connection_table.png      -> STAAD member force table screenshot used to confirm the
                               maximum axial force (shown under the Member Axial Force Summary).

DEFLECTION CHECK:
  deflection_vertical_table.png    -> STAAD GUI table showing maximum vertical displacement
                                      for the SLS combination
  deflection_horizontal_table.png  -> STAAD GUI table showing maximum horizontal displacement
                                      for the SLS combination

Missing load diagrams show as labelled placeholder boxes in the report.
Missing connection_table / deflection table images are simply left out of the report.
