# -*- coding: utf-8 -*-
"""
@time: 2016
@author: zhw
"""

import numpy as np
from pyswarm import pso
import matplotlib.pyplot as plt
#################################
# test 3 #
#author: zhw
#time: 2016/11/21
#################################
print('*'*65)
print('Example minimization of 4th-order T3 function (with constraints)')

## 1.define upper fitness function, min x
def upper_func(x, *args_y):
    x1 = x
    y1, = args_y
    return x1**2+(y1-10)**2

#define upper constraint
def upper_con(x, *args_y):
    x1 = x
    y1, = args_y
    return [-x1-2*y1+6]
###################

## 2.define down fitness function, min y
def down_func(y, *args_x):
    y1 = y
    x1, = args_x
    return x1**3-2*y1**3+x1-2*y1-x1**2

#define down constraint
def down_con(y, *args_x):
    y1 = y
    x1, = args_x
    return [x1-2*y1+3]

## 3. init 
COUNT_MAX = 100

lb_x = [0]
ub_x = [50]

lb_y = [0]
ub_y = [20]

y1_c = 10
args_y = (y1_c,)

x1_c = 10
args_x = (x1_c,) 

result = np.zeros(COUNT_MAX)

## 4. do pso for optimation
for i in range(COUNT_MAX):
	print '*'*30
	print 'iteration {}'.format(i)
	# optimize for upper agent
	xopt, upper_fopt = pso(upper_func, lb_x, ub_x, f_ieqcons=upper_con, args=args_y, swarmsize=20, omega=1.0, phip=2.5, phig=2.5, debug=False, maxiter=120)
	# x1_c, x2_c = xopt
	args_x = tuple(xopt)
	print 'x1 is {}'.format(args_x)
	print('    optimize upper function: {}'.format(upper_fopt))
    # optimize for down agent
	yopt, down_fopt = pso(down_func, lb_y, ub_y, f_ieqcons=down_con, args=args_x, swarmsize=40, omega=0.9, phip=2.5, phig=2.0, debug=False, maxiter=30)
	args_y = tuple(yopt)
	print 'y1 is {}'.format(args_y)
	print('    optimize down function: {}'.format(upper_fopt))
	result[i] = upper_fopt
     #result[i] = down_fopt
	i += 1

plt.plot(result)
plt.show()
print('The optimum is at:')
print('    xopt{}'.format(xopt))
print('    yopt{}'.format(yopt))
print('Optimal function value:')
print('    optimize upper function: {}'.format(upper_fopt))
print('    optimize down function: {}'.format(down_fopt))
