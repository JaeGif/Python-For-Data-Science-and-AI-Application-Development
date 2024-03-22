import numpy as np

# numpy is a library used for working with arrays,
# linear algebra and matrices
# can cast lists to a np arr

sample = [[0, 1], [0, 1], [0, 2], [0, 3], [0, 4]]

a = np.array(sample)
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
b[0] = 100
b[1] = 20
even = a[::2]
select = [0, 2, 3, 4]
c = a[select]
mean = a.min()

d = np.array([-10, 201, 43, 94, 502])

u = np.array([1, 0])
v = np.array([0, 1])
z = np.add(u, v)
print(u + v, z)
