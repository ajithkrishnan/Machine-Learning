import numpy as np 

# Define sigmoid function
def nonlin(x,deriv=False):
    out = 1/(1 + np.exp(-x))
    if(deriv==True):
        return out*(1-out)
    return out
    
# Input dataset
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])

# Output dataset
y = np.array([[0,0,1,1]]).T    

# seed random numbers to make calculation
# more deterministic
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2*np.random.random((3,1)) - 1

for iter in xrange(10000):

    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))
    if(iter == 1):
        l1_first = l1

    # by how much did we miss?
    l1_error = y - l1
    if(iter % 2000 == 0):
        print("Error at %dth iteration:" %iter)
        print l1_error

    # printing the value of the slope of the sigmoid function at 
    # the values of X(or l1)
    if(iter % 2000 == 0):
        slope = nonlin(l1,True)
        print("Gradients at %dth iteration:" %iter)
        print slope


    # multiply the error with the slope of the 
    # sigmoid function at the values in l1
    l1_delta = l1_error*nonlin(l1,True)
    if(iter % 2000 == 0):
        print("Delta at %dth iteration:" %iter)
        print l1_delta

    # update weights
    syn0 += np.dot(l0.T,l1_delta)
    if(iter % 2000 == 0):
        print("Weight at %dth iteration:" %iter)
        print syn0

print "Output after first iteration:"
print l1_first
print "Output after training:"
print l1
