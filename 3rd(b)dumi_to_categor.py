    ##B. Perform feature Dummification to convert categorical variables into numerical representations. 
Code:

import pandas as pd
iris=pd.read_csv("D:\\data science\\Iris.csv")
print(iris)
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
iris['code']=le.fit_transform(iris.Species)
print(iris)
