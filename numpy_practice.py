import pandas as pd
import numpy as np

# 1. Use arange to create an array of the numbers from 0 to 100.
a  = np.arange(101)
print "Array of the numbers from 0 to 100: ", '\n', a, '\n'

# 2. Create two arrays [1, 3, 5] and [2, 4, 6] and add them.
x = [1, 3, 5]
y = [2, 4, 6]
z = np.add(x,y)
print "Adding [1, 3, 5] and [2, 4, 6]: ", '\n', z, '\n'

# 3. Create a 3-by-6 matrix and then find out its dimensionality using ndim.
m = np.matrix([[1,2,3,4,5,6], [11, 12, 13, 14, 15, 16], [21, 22, 23, 24, 25, 26]])
print "matrix m: ", '\n', m, '\n'
print "Dimensions of m: ", m.ndim 
print "shape of m: ", m.shape

# 4. In the aforementioned matrix, use dtype to discover the data types within the matrix.
print "Data types within the above matrix: ", m.dtype, '\n'


# 5. Create a 4-by-5 matrix full of zeros using zeros.
z = np.zeros((4,5))
print "4-by-5 matrix full of zeros: ", '\n', z, '\n'

#    Then, create a 5-by-4 matrix full of ones using ones.
o = np.ones((5,4))
print "5-by-4 matrix full of ones: ", '\n', o, '\n'

# 6. Use reshape to turn the array from Question 1 into a 10-by-10 matrix.
ai = a[0:100]
#am = np.asmatrix(ai.reshape(10,10))
am = ai.reshape(10,10)
print "10-by-10 matrix: ", am, '\n'

# 7. Given two 2-by-2 arrays A and B of your creation, do A * B and dot(A, B). What's the difference?
Aa = np.arange(4)
A = Aa.reshape(2,2)

Bb = np.arange(4)
B = Bb.reshape(2,2)

print "A * B is: ", '\n', A * B, '\n'
print "dot(A,B) is: ", '\n', np.dot(A,B), '\n'


# 8. Given the array in Question 1, set every 2nd element to 31415. (Hint: use the third parameter in list slicing)
a  = np.arange(101)
a[::2] = 31415
print "Set every 2nd element of a to 31415: ", '\n', a, '\n'


# 9. Write a function that takes any arbitrary multidimensional array (aka matrix) 
# and returns just the nth column. Hint: the function will look like def retrieve_column(matrix, n).
def retrieve_column(matrix, n):
    return matrix[:,n]

print "Input matrix is: ", '\n', am, '\n' 
print "nth column: ", '\n', retrieve_column(am, 1)