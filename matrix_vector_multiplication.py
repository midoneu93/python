import numpy as np

m = np.matrix('1, 2, 3; 4, 5, 6;7, 8, 9')
v = np.matrix('1; 1; 1')

mv = m*v

print(m)
print(v)
print(mv)