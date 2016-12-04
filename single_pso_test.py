import numpy as np
from pyswarm import pso

###############################################################################

print('*'*65)
print('Example minimization of 4th-order banana function (no constraints)')
def myfunc(x):
    X = x[0]
    Y = x[1]
    return X**2-X+7

lb = [-2, -2]
ub = [2, 2]

xopt1, fopt1 = pso(myfunc, lb, ub, swarmsize=20, omega=1.0, phip=0.49, phig=1.49, debug=True, processes=1, maxiter=3000)

print('The optimum is at:')
print('    {}'.format(xopt1))
print('Optimal function value:')
print('    myfunc: {}'.format(fopt1))

###############################################################################


