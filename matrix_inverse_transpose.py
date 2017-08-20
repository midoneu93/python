import numpy as np

m = np.matrix('3, 4; 2, 10')

print('m =\n', m)
print('mi =\n', m.getI())
print('mi * m =\n', m.getI() * m)



a = np.matrix('1, 2, 0; 3, 5, 9')

print('a =\n', a)
print('at =\n', a.getT())
