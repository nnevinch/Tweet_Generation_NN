import pandas as pd
import sys

name = sys.argv[1]
file_in = name+'_10000.csv'

df = pd.read_csv(file_in, names = ['date','username','to','replies','retweets','favorites','tweet','geo','mentions','hashtags','id','permalink'], header=1)
df.to_csv(file_in, index=False)

