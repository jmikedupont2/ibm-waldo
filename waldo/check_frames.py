import pandas as pd
import numpy as np
import os
from tqdm import tqdm


path = os.path.join('jester-v1-train-five.csv')
df = pd.read_csv( path,index_col = None,header=None,sep=';')
df.columns = ['Folder','Action','Frames']

x = df[df['Frames']>=35].groupby('Action').count()
print(x)
