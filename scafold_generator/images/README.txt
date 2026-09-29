IMAGES FOLDER - NAMING GUIDE
=============================
Drop STAAD.Pro screenshots here with exactly these filenames.
Supported extensions: .png, .jpg, .jpeg

3D MODEL:
  3d_model.png              -> 3D isometric view. Generated automatically when
                               AUTO_RENDER_3D_MODEL is "yes" in project_info.txt
                               (overwritten on every run), otherwise drop your own.

LOAD DIAGRAMS:
  load_platform_live.png    -> Platform live load diagram
  load_handrail_x.png       -> Handrail load X-axis diagram, when applicable
  load_handrail_z.png       -> Handrail load Z-axis diagram, when applicable
  load_wind_x.png           -> Wind load X-axis diagram (only if the model has wind loads)
  load_wind_z.png           -> Wind load Z-axis diagram (only if the model has wind loads)

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
