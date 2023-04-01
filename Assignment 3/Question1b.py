import numpy
from numpy.linalg import eig

list = [3, -2, 1, 0]
arr = numpy.array(list).reshape(2,2)
eigenvalues,eigenvectors=eig(arr)
print('Eigenvalue:', eigenvalues)
print('Eigenvector', eigenvectors)
