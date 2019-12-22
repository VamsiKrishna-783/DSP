import numpy as np
M=np.array(input("Enter the Matrix M:"))
N=np.array(input("Enter the Matrix N:"))
print "The det of M is:",np.linalg.det(M)
print "The Rank Of N is:",np.rank(N)
print "The max value of M is:",np.max(M)
print "The min value of N is:",np.min(N)
print "The Transpose of matrix N is:",np.transpose(N)
print "The Zero matrix:",np.zeros((3,3))
print "The eigen values of matrix M:",np.linalg.eig(M)
print "The Trace of Matrix N:",np.trace(N)
print "The inverse of Matrix M:",np.linalg.inv(M)


