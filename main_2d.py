
"""
I made my own version of the K Nearest Neighbors algorithm using just python and numpy.

It only works with 1 neighbor, with a 2D array.

This is a made up dataset about the size of grocery bags

0 = small
5 = medium
7 = large

first column of X_train is weight of grocery bags
second column of X_train is height of grocery bags
"""
import matplotlib.pyplot as plt
import numpy as np
# The Data
X_train = np.array([[1, 2],       
           [2, 4],
           [4, 3],
           [6, 10],
           [8, 11],
           [9, 13],
           [20,25],
           [35,30]]) # features, descriptions, attributes, can be any number
y_train = [1,1,1,5,5,5,7,7] # targets, labels, type, can be any character defining the numbers
X_test = np.array([[-10,4],[1,2],[4,6],[7,9],[3,1],[10,0],[6,7],[0.5,0.1],[0.7,0.9],[40,19],[30,25]]) # the data that you want to see its nearest neighbors
y_test = [1] # this should never be used in the code, it's always here for double checking 

# the distance between X_test and all of the numbers in X_train will 
# be sorted in absolute value (no negatives)

def knn_recreation(xtest):

    counter = 0
    
    Xdist = []
    
    for i in range(len(X_train)):
            
        ColumnOneDifference = abs(X_train[i][0] - xtest[0])
        ColumnTwoDifference = abs(X_train[i][1] - xtest[1])
        Xdist.append(ColumnOneDifference + ColumnTwoDifference) 
        
        
    distSorted = sorted(Xdist) # Saving the distance between x_test and all of the numbers in X_train for the future
        
    
    # This loop finds the index of X_test's nearest neighbor, and then saves the answer.
    closestBagIndex = 0
    
    for x in Xdist:
        if x == distSorted[0]:
            break
        closestBagIndex += 1
        


    print(y_train[closestBagIndex])
    print(X_train[closestBagIndex])

    return(y_train[closestBagIndex])

y_pred = []

for data in X_test:
    y_pred.append(knn_recreation(data))

print(y_pred)

# graphing

plt.scatter(X_test[:,0],X_test[:,1],c=y_pred,marker="x") 

plt.scatter(X_train[:,0],X_train[:,1],c=y_train) #marker="x")
plt.colorbar()
