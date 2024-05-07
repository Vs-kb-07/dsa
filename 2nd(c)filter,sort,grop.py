C.	Manipulate and transform data using functions like filtering, sorting, and grouping
 Code:

import pandas as pd 
# Load iris dataset 
iris = pd.read_csv('Iris.csv') 

# Filtering data based on a condition 
setosa = iris[iris['Species'] == 'setosa'] 
print("Setosa samples:") 
print(setosa.head()) 

# Sorting data 
sorted_iris = iris.sort_values(by='SepalLengthCm', ascending=False) print("\nSorted iris dataset:")
print(sorted_iris.head())

# Grouping data 
grouped_species = iris.groupby('Species').mean() 
print("\nMean measurements for each species:") 
print(grouped_species)
