 B.(1)	# Replacing NA values using fillna()

import pandas as pd
df = pd.read_csv('titanic.csv') 
print(df)
df.head(10)
print("Dataset after filling NA values with 0 : ")
df2=df.fillna(value=0)
print(df2)

  (2)	# Dropping NA values using dropna() 

import pandas as pd
df = pd.read_csv('titanic.csv') 
print(df)
df.head(10) 
print("Dataset after dropping NA values: ") 
df.dropna(inplace = True)
print(df)
