import numpy as np
n=input("Enter the length of array:")
A=np.array(input("Enter the A matrix:"))
V=input("Enter the no.0f colums in A:")
B=np.array(input("Enter the B matrix:"))
M=input("Enter the no.of rows in B:")
result=np.zeros((V,M))
for i in range(len(A)):
	for j in range(len(B[0])):
		for k in range(len(B)):
			result[i][j]+=A[i][k]*B[k][j]
for r in result:
	print(r)
