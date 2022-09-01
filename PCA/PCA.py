# Principal Component analysis of YidC protein MD trajectories
#
# Requires package prody
#
# Usage with aligned C-alpha trajecories for individual systems
# python eda.py

from prody import *
from numpy import *
from string import Template
struct = parsePDB('input.pdb')
traj = Trajectory('')

traj.addFile('input.dcd')

traj.link(struct)
traj.setCoords(struct)
traj.setAtoms(struct.ca)

eda=EDA('all')
eda.buildCovariance(traj)
eda.calcModes()
saveModel(eda)

#eda = loadModel("papc.pca.npz")

writeNMD('eda-all.nmd', eda[:20], struct.ca)
trajs=traj[:]
trajs.superpose()
proj = calcProjection(trajs,eda[:20],rmsd=True, norm=False)
writeArray("projection-all.txt",proj,format="%f")
fract=calcFractVariance(eda[:20])
writeArray("fract-all.txt",fract,format="%f")
fract=calcFractVariance(eda[:20])
writeArray("fract-all.txt",fract,format="%f")

quit()
