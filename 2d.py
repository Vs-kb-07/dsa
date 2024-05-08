import pandas as pd
df = pd.read_csv(r'C:\Users\ANKIT SINGH\OneDrive\Desktop\pra2\data.csv')
print(df)
df.head(10)
print("Dataset after dropping NA values: ")
df.dropna(inplace = True)
print(df)
