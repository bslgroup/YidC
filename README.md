###Script and Macros Used for Analysis of MD Trajectories of YidC Studied in Article: Deciphering the Inter-domain Decoupling in the Gram-negative Bacterial Membrane Insertase Authors: Adithya Polasa and Mahmoud Moradi

#Dynamic Network Analysis (calc_correlation_custom.py)

This is done using python package MD-TASK, software suite of MD analysis tools, was used to calculate the correlation coefficient for the motion of each C_alpha atom relative to the other C_alpha atoms. A correlation matrix M was generated for each of the three protomers in all the simulated trajectories. Additionally, a correlation matrix for the entire trimer was calculated for each simulation to explore correlations between structures of different protomers.

#Hydrogen Bond Analysis (hbond.tcl)

#Principal Component analysis (PCA) (PCA.py)

PCA performed with ProDy using this python script to quantify the persistent conformational changes and relative motions of the active and inactive states.

#Root Mean Square Deviation (RMSD) (RMSD.tcl)

#Salt-Bridge Analysis (salt.tcl)

#Transmembrane Helical Angle (inter_helical_angle.tcl)

These are VMD scripts For the inter helical angle calculations, we chose residues of indivual helices of YidC Transmembrane region. The angle script measures, vector angle between the helix 1 and Helix 2 and computed angle was subtracted from 180◦.

#Water Analysis (water.tcl)
The amount of solvent water inside the groove quantified using water analysis VMD script. This calculates the number of water molecules within 5 ̊A of the R366 for every frame of trajectory.
