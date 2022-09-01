#Script and Macros Used for Analysis of MD Trajectories of YidC Studied in Article: Deciphering the Inter-domain Decoupling in the Gram-negative Bacterial Membrane Insertase Authors: Adithya Polasa and Mahmoud Moradi

#Distance (distances-CoV2.tcl and distances-CoV1.tcl)

This VMD scripts calculates the RBM-S2 distance, center of mass based on residues that form a beta-sheet in the RBM region of each RBD. This distance script measures the vector distance between the two center of mass and used the vector magnitude to output the overall distance.

#Angle (angle-CoV2.tcl and angle-CoV1.tcl)

These are VMD scripts For the RBM-S2 angle calculations, we chose residues at the top and bottom of the straightest region of the S2 Trimer. The angle script measures, vector angle between the RBD and S2 was then calculated with the following equation:arccos(v1·v2/|v1||v2|) then computed angle was subtracted from 180◦.

#Dynamic Network Analysis (calc_correlation_custom.py)

This is done using python package MD-TASK, software suite of MD analysis tools, was used to calculate the correlation coefficient for the motion of each C_alpha atom relative to the other C_alpha atoms. A correlation matrix M was generated for each of the three protomers in all the simulated trajectories. Additionally, a correlation matrix for the entire trimer was calculated for each simulation to explore correlations between structures of different protomers.

#Principal Component analysis (PCA) (pca_out_select.py)

PCA performed with ProDy using this python script to quantify the persistent conformational changes and relative motions of the active and inactive states.

#Water Analysis (do_water.sh)
