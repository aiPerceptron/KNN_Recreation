"""
I made my own version of the K Nearest Neighbors algorithm using just python.

It only works with 1 neighbor, with a 1D array.

"""

X_train = [1,      2,      3,        2.1,   4,       3.5,     7,     6] # features, descriptions, attributes, can be any number
y_train = ["small","small","medium","small","medium","small","large","large"] # targets, labels, type, can be any character defining the numbers
X_test = int(input("input your data: ")) # the data that you want to see its nearest neighbors
y_test = 1 # the answer to see if your ML algorithm is right.

Xdist = [] 

# the distance between X_test and all of the numbers in X_train will 
# be sorted in absolute value (no negatives)

for x in X_train:
    Xdist.append(abs(x - X_test)) 

distSorted = sorted(Xdist) # Saving the distance between x_test and all of the numbers in X_train for the future
print(distSorted[0]) 

numIndex = 0 # Index of X_test's nearest neighbor.

# This loop finds the index of X_test's nearest neighbor, and then saves the answer.

for x in Xdist: 
    if x == distSorted[0]:
        # print(x)
        # print(numIndex)
        break
    numIndex += 1


# print(X_train[numIndex]) # prints the nearest neighbor of X_test
# print(y_train[numIndex]) # prints the target of the nearest neighbor of X_test
y_pred = [y_train[numIndex]] # the prediction
print(y_pred)
