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
    x1, x2 = x
    y1, y2 = args_y 
    return -x1**2-3*x2-4*y1+y2**2

#define upper constraint
def upper_con(x, *args_y):
    x1, x2= x
    y1, y2 = args_y
    return [4-x1**2-2*x2]

###################

## 2.define down fitness function, min y
def down_func(x, *args_x):
    y1, y2 = x
    x1, x2 = args_x
    return 2*x1**2+y1**2-5*y2

#define down constraint
def down_con(x, *args_x):
    y1, y2 = x
    x1, x2 = args_x
    return [x1**2-2*x1+x2**2-2*y1+y2+3, x2+3*y1-4*y2-4]

## 3. init 
COUNT_MAX = 100

lb_x = [0, 0]
ub_x = [1000, 1000]

lb_y = [0, 0]
ub_y = [1000, 1000]

y1_c = 10
y2_c = 10
args_y = (y1_c, y2_c)

x1_c = 10
x2_c = 10
args_x = (x1_c, x2_c) 

x1 = 10000
x2 = 10000

y1 = 10000
y2 = 10000

result = np.zeros(COUNT_MAX)

## 4. do pso for optimation
for i in range(COUNT_MAX):
	print '*'*10
	print 'iteration {}'.format(i)
	# optimize for upper agent
	xopt, upper_fopt = pso(upper_func, lb_x, ub_x, f_ieqcons=upper_con, args=args_y, swarmsize=500, omega=1.0, phip=0.5, phig=1.5, debug=False, processes=1, maxiter=200)
	# x1_c, x2_c = xopt
	args_x = tuple(xopt)
	print 'x1, x2 is {}'.format(args_x)
	print('    optimize upper function: {}'.format(upper_fopt))
    # optimize for down agent
	yopt, down_fopt = pso(down_func, lb_y, ub_y, f_ieqcons=down_con, args=args_x, swarmsize=500, omega=1.0, phip=0.5, phig=1.5, debug=False, processes=1, maxiter=200)
	args_y = tuple(yopt)
	# print 'y1, y2 is {}'.format(args_y)
	result[i] = upper_fopt
	i += 1

plt.plot(result)
plt.show()
print('The optimum is at:')
print('    xopt{}'.format(xopt))
print('    yopt{}'.format(yopt))
print('Optimal function value:')
print('    optimize upper function: {}'.format(upper_fopt))
print('    optimize down function: {}'.format(down_fopt))
# print('    constraints : {}'.format(mycon(xopt2)))



