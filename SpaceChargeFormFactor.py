from numpy import *
import pylab as pl

# p      f    1/p     f
FormF = array([
[0.00, 1.000, 0.00, 0.000],
[0.05, 0.926, 0.05, 0.007],
[0.10, 0.861, 0.10, 0.020],
[0.15, 0.803, 0.15, 0.037],
[0.20, 0.750, 0.20, 0.056],
[0.25, 0.704, 0.25, 0.075],
[0.30, 0.661, 0.30, 0.095],
[0.35, 0.623, 0.35, 0.115],
[0.40, 0.588, 0.40, 0.135],
[0.45, 0.556, 0.45, 0.155],
[0.50, 0.527, 0.50, 0.174],
[0.55, 0.500, 0.55, 0.192],
[0.60, 0.476, 0.60, 0.210],
[0.65, 0.453, 0.65, 0.227],
[0.70, 0.432, 0.70, 0.244],
[0.75, 0.413, 0.75, 0.260],
[0.80, 0.394, 0.80, 0.276],
[0.85, 0.378, 0.85, 0.291],
[0.90, 0.362, 0.90, 0.306],
[0.95, 0.347, 0.95, 0.320],
[1.00, 0.333, 1.00, 0.333]],float)

X = linspace(0,1,100)
C =  polyfit(FormF[:,0],FormF[:,1],4)
Cinv = polyfit(FormF[:,2],FormF[:,3],4)

print C
print Cinv

Y = polyval(C,X)
Yinv = polyval(Cinv,X)

if True:
	pl.figure(); pl.plot(X,Y); pl.plot(FormF[:,0],FormF[:,1],'.')
	pl.figure(); pl.plot(X,Yinv); pl.plot(FormF[:,2],FormF[:,3],'.')
	pl.show()

# Fit results:
# polynomial coefficients 
# C = [ 0.32685993 -1.10422029  1.64157723 -1.52987752  0.99919503]
# Cinv = [ 0.39122685 -0.97242357  0.74316934  0.1744343  -0.0020169 ]

