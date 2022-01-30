import pandas as pd
import numpy as np
import sys
print ('Number of arguments:', len(sys.argv), 'arguments.')
if(len(sys.argv)!=2):
    print("Please provide file name")
    exit()
else:
    print("File name:", sys.argv[1] )    
    tsvFileName=sys.argv[1]
    '''Tsv File read here'''
    weather_df = pd.read_csv(tsvFileName, sep='\t')
    print(weather_df)




