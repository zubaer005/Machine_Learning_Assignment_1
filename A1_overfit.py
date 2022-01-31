import pandas as pd
import numpy as np
import sys
import csv
import random
import math
import operator


def handleDataset(split):
    global trainingSet  
    global testSet   
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    if(len(sys.argv)!=2):
        print("Please provide file name")
        exit()
    else:
        print("File name:", sys.argv[1] )    
        filename=sys.argv[1] 
        df  = pd.read_csv(filename, sep='\t')   
        testSet = df.sample(frac = split)  
        trainingSet = df.drop(testSet.index)  
         

def main():
     
    handleDataset(0.25)
    print ('Train: ' + repr(len(trainingSet)))
    print ('Test: ' + repr(len(testSet)))
        
main()




