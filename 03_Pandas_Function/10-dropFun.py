import pandas as pd
import numpy as np

D1=pd.read_csv("D:\\LEARN_PYTHON\\Day-21_Pandas_lib\\03_Pandas_Function\\customers-100.csv")
print(D1)

print(D1.drop("Website",axis=1)) # .drop() function is used to drop the column from the DataFrame. Here we are dropping the "Website" column from the DataFrame

print(D1.drop([0,1],axis=0)) # .drop() function is used to drop the rows from the DataFrame. Here we are dropping the first 2 rows (index 0 and 1) from the DataFrame