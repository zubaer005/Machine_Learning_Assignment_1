import csv
import random
import math
import operator 
#read the datafream
def handleDataset(filename, split, trainingSet=[] , testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4): 
                dataset[x][y] = float(dataset[x][y]) 
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])
#calculate the distance
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2) 
    return math.sqrt(distance)
#find the k Neighbors
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length) 
        distances.append((trainingSet[x], dist))
    
    distances.sort(key=operator.itemgetter(1))
     
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    
    return neighbors

trainingSet = [[2, 2, 2, 'a'], [4, 4, 4, 'b']]
testInstance = [5, 5, 5]
k = 1
neighbors = getNeighbors(trainingSet, testInstance, 1)
print(neighbors)

'''
trainingSet=[]
testSet=[]
handleDataset(r'iris.data.txt', 0.66, trainingSet, testSet)
print ('Train: ' + repr(len(trainingSet)))
print ('Test: ' + repr(len(testSet)))

data1 = [2, 2, 2, 'a']
data2 = [4, 4, 4, 'b']
distance = euclideanDistance(data1, data2, 3)
print ('Distance: ' + repr(distance))
'''
