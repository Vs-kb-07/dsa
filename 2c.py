import pandas as pd
df = pd.read_csv(r'C:\Users\ANKIT SINGH\OneDrive\Desktop\pra2\data.csv')
print(df)
df.head(10)
print("Dataset after filling NA values with 0 : ")
df2=df.fillna(value=0)
print(df)

