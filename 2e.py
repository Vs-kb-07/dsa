import pandas as pd
iris = pd.read_csv(r'C:\Users\ANKIT SINGH\OneDrive\Desktop\pra2\Iris.csv')
setosa = iris[iris['Species'] == 'setosa']
print("Setosa samples:")
print(setosa.head())
sorted_iris = iris.sort_values(by='SepalLengthCm', ascending=False)
print("\nSorted iris dataset:")
print(sorted_iris.head())
grouped_species = iris.groupby('Species').mean()
print("\nMean measurements for each species:")
print(grouped_species)
