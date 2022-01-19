import matlab.engine
import numpy as np
from numpy import array, arange
from matlab import double as double_m

eng = matlab.engine.start_matlab()
eng.desktop(nargout=0)
eng.workspace['x'] = 3
a = eng.eval("x+3;")

eng.eval("y = 5;", nargout=0)
print(eng.workspace['y'])
x_matlab = eng.linspace(0.0, 1000.0, 1000)
x_py = array(x_matlab)

eng.eval('x = linspace(0, 1000, 1000)', nargout=0)
x_py = array(eng.workspace['x'])

eng.addpath('/home/kkk/matlab_utility', nargout=0)

x_randn_matlab = eng.randn(4,4)
x_randn_matlab_T = eng.transpose(x_randn_matlab)

y = arange(16).reshape(4, 4)
y_matlab = double_m(y.tolist(), is_complex=True)
eng.workspace['y'] = y_matlab

eng.quit()

print(y_matlab)