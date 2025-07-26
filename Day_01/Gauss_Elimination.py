import numpy as np    

#perfrom Gaussian elimination (GE) for the lineary system Ax=b
#on return, the matrix A is destroyed. The solution is
#stored in x. 
def GE(A,b):
    n = len(b)
   
    # forward elimination
    for k in range(0,n-1):
        for i in range(k+1,n):
            if abs(A[k,k]) > 1E-8:
                factor = A[i,k]/A[k,k]
                A[i,:] = A[i,:] - factor*A[k,:]
                b[i] = b[i] - factor*b[k]
            else:
                sys.exit("Singular on diagonal. Pivoting is needed.")
    
    # back substitution
    x = np.zeros(n)
    for k in range(n-1,-1,-1):
        x[k] = (b[k] - np.dot(A[k,k+1:n],x[k+1:n]))/A[k,k]
    return x

#define the matrix and vector
A = np.array([[2.0,3.0,5.0], [4.0,-5.0,-7.0], [1.0,2.0,-3.0]])
b = np.array([1.0,6.0,2.0])

#call the Gaussian elimination function
x = GE(A,b)

#print out solution
print("solution = ", x)