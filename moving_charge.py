import matplotlib.pyplot as plt
import numpy as np

from ipywidgets import interact, interactive
import ipywidgets as widgets

!{sys.executable} -m pip install --quiet matplotlib
'''
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rcParams['font.size'] = 15
'''
#  Begin edit

beta = 0.5
plt.title( r"$\beta = 0.5$" )
plt.ylim( -0.5, 1.5 )

#  End edit

def plot_dif_beta(beta)
	gamma = 1. / np.sqrt( 1. - np.power( beta, 2 ) )

	tp = np.linspace( -1001, 1001, 10001 ) / 100.

	denom = np.power( 1. + np.power( tp, 2 ), 3./2. )

	Ex = -tp / denom
	Ey =  gamma / denom
	Bz = beta * gamma / denom

	plt.plot(tp, Ex, label=r"$E_x / E_0$" )
	plt.plot(tp, Ey, label=r"$E_y / E_0$" )
	plt.plot(tp, Bz, label=r"$B_z / E_0$" )

	plt.legend(loc='upper left', shadow=True)

	plt.xlabel( '$t / t_0$' )

	plt.xlim( -10, 10 )

	plt.show()


interact(plot_with_slope, beta = widgets.BoundedFloatText(value=0.5, min=0.01, max = 1, step=0.01, 
                                                       descriptions='beta', disabled=False))
