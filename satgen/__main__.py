n = 10
m = 5
k = 3

from . import Instance, Distribution

sat = Instance(n, m, k)
sat.generate()

print(sat)
