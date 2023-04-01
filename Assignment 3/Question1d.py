import numpy

list = [1, 2, 3, 4, 5, 6]
arr = numpy.array(list).reshape(3,2)
print(arr)
arr = numpy.array(arr).reshape(2,3)
print(arr)
