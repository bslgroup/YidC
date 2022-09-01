package require hbonds 

mol new input.psf
mol addfile input.dcd type dcd first 0 last -1 step 1 filebonds 1 autobonds 1 waitfor all
set all [atomselect $i "all"]
set TM4 [atomselect $i "protein and resid 516 and sidechain"]
set TM5 [atomselect $i "protein and resid 429 and sidechain"]

hbonds -sel1 $TM4 -DA both -sel2 $TM5 -DA both -dist 4.0 -ang 30 -polar yes -type unique -writefile yes -outdir outputname-0 -log outputname.log -outfile outputname.hbonds.dat -detailout outputname.stdout

quit
