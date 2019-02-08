import pandas as pd 

data = pd.read_csv("data/count.csv")
data = data.set_index('word')
data.sort_values(by='date',ascending=False,inplace=True)

