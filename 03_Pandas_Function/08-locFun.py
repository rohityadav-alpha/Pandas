import pandas as pd
import numpy as np

D1=pd.read_csv("D:\\LEARN_PYTHON\\Day-21_Pandas_lib\\03_Pandas_Function\\customers-100.csv")
print(D1)

D1.loc[0,"website"] = "www.example.com" # .loc function is used to access a group of rows and columns by labels or a boolean array. Here we are changing the value of the "website" column for the first row (index 0) to "www.example.com"
print(D1)

print(D1.loc[[0,5],["FirstName","LastName"]]) # .loc function is used to access a group of rows and columns by labels or a boolean array. Here we are accessing the first 5 rows (index 0 to 5) and the "FirstName" and "LastName" columns

# D1["website"][1] = "www.example.com" # Here we are changing the value of the "website" column for all rows to "www.example.com"
# print(D1)