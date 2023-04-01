import numpy

list = [0, 1, 2, 3, 4, 5]
arr = numpy.array(list).reshape(2,3)
trace = numpy.trace(arr)
print(trace)
