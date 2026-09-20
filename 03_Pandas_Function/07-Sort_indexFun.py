import pandas as pd
import numpy as np

D1=pd.read_csv("D:\\LEARN_PYTHON\\Day-21_Pandas_lib\\03_Pandas_Function\\customers-100.csv")
print(D1)

print(D1.sort_index(axis=0)) # .sort_index() function is used to sort the DataFrame by index values in ascending order
print(D1.sort_index(axis=0,ascending=False)) # .sort_index(ascending=False) function is used to sort the DataFrame by index values in descending order 

print(D1.sort_index(axis=1)) # .sort_index(axis=1) function is used to sort the DataFrame by column names in ascending order
print(D1.sort_index(axis=1,ascending=False)) # .sort_index(axis=1,ascending=False) function is used to sort the DataFrame by column names in descending order