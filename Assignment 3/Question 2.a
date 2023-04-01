import numpy
import random

list = [random.randint(1,20), random.randint(1,20), random.randint(1,20), random.randint(1,20), random.randint(1,20), random.randint(1,20), random.randint(1,20), random.randint(1,20), random.randint(1,20), random.randint(1,20), random.randint(1,20), random.randint(1,20), random.randint(1,20), random.randint(1,20), random.randint(1,20)]
vector = numpy.array(list).reshape((3,5))
print("Original vector after reshape")
print(vector)
print("Shape of vector")
print(numpy.shape(vector))
#numpy.where(numpy.isin(vector,max), 0, vector)
maxNum = numpy.amax(vector, axis=1)
vector[vector == maxNum[:, None]] = 0
print("Vector after replacing max with 0")
print(vector)
