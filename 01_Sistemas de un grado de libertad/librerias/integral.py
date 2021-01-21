# Metodo de la Cuadrantura de Gauss para calcular integrales numericamente
import numpy as np

def cuad_gauss(t0,tf,f):
	w = [[1,1],
	[0.55555,0.88888,0.55555],
	[0.3478548451,0.6521451549,0.6521451549,0.3478548451],
	[0.2369268851,0.4786286705,0.5688888888,0.4786286705,0.2369268851],
	[0.1713244924,0.3607615730,0.4679139346,0.4679139346,0.3607615730,0.1713244924],
	]

	z = [[-0.5773502692,0.5773502692],
	[-0.7745966692,0,0.7745966692],
	[-0.8611363116,-0.3399810436,0.3399810436,0.8611363116],
	[-0.9061798459,-0.5384693101,0,0.5384693101,0.9061798459],
	[-0.9324695142,-0.6612093865,-0.2386191861,0.2386191861,0.6612093865,0.9324695142],
	]

	n = 4	# número de puntos a emplear: 2,3,4,5,6  obs:se recomienda 3 puntos mínimo

	k = (tf - t0)/2
	w1 = w[n - 2]
	z1 = z[n - 2]
	I = 0
	for i in range(len(w1)):	
		I = I + w1[i]*f(z1[i] * (tf - t0)/2 + (t0 + tf)/2)
	return round(I*k, 5)
