import sympy as sym
from sympy.plotting import plot
sym.init_printing(use_unicode=True) %matplotlib inline

expr = x**2-12*x+8

plot(expr, (x, -20, 20))