import pandas as pd 


data = pd.read_csv("../data/count.csv")
data = data.set_index('word')
data.sort_values(by='date',ascending=False,inplace=True)

res = data.index.value_counts()

keys = res.keys()
values = res.values

print("<<<<<<< the most frequency words are as follow: <<<<<<<<")
print(pd.Series(values[:10],index=keys[:10]))