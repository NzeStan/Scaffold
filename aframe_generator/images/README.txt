IMAGES FOLDER - NAMING GUIDE
==============================
Drop STAAD.Pro screenshots here with EXACTLY these filenames.
Supported extensions: .png  .jpg  .jpeg

3D MODEL:
  3d_model.png              -> 3D isometric view. Generated automatically when
                               AUTO_RENDER_3D_MODEL is "yes" in project_info.txt
                               (overwritten on every run), otherwise drop your own.

LOAD DIAGRAMS:
  load_chain_hoist.png      -> Chain hoist load diagram (CHAIN HOIST LOAD)
  load_impact_x.png         -> Impact load X-axis diagram (IMPACT LOAD ON X-AXIS)
  load_impact_z.png         -> Impact load Z-axis diagram (IMPACT LOAD ON Z-AXIS)
  load_wind_x.png           -> Wind load X-axis diagram (only if the model has wind load cases)
  load_wind_z.png           -> Wind load Z-axis diagram (only if the model has wind load cases)

  One diagram is needed per hoist load case. The first case uses the names above; every
  further case (TITLE ...-1, ...-2, etc.) adds a numbered file:
  load_chain_hoist_1.png, load_chain_hoist_2.png ...   -> CHAIN HOIST LOAD-1, -2 ...
  load_impact_x_1.png,    load_impact_x_2.png ...      -> IMPACT LOAD ON X-AXIS-1, -2 ...
  load_impact_z_1.png,    load_impact_z_2.png ...      -> IMPACT LOAD ON Z-AXIS-1, -2 ...
  The report shows as many diagrams as the model has cases (captioned "Chain Hoist Load
  (CL)-1" etc.).

WIND CALCULATION:
  (no extra images - wind calc is fully computed from the .std file)

CONNECTION STABILITY CHECK:
  connection_table.png      -> STAAD member force table screenshot used to confirm the
                               maximum axial force (shown under the Member Axial Force Summary).

DEFLECTION CHECK:
  deflection_vertical_table.png    -> STAAD GUI table showing max vertical displacement
                                      (for the SLS combination you recorded in project_info.txt)
  deflection_horizontal_table.png  -> STAAD GUI table showing max horizontal displacement

Missing load diagrams show as labelled placeholder boxes in the report.
Missing connection_table / deflection table images are simply left out of the report.
