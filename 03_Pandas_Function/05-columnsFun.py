import pandas as pd

D1=pd.read_csv("D:\\LEARN_PYTHON\\Day-21_Pandas_lib\\03_Pandas_Function\\customers-100.csv")
print(D1)

print(D1.columns) # .columns function is used to get the column names of the DataFrame

print(D1.columns.array) # .columns.array function is used to get the column names of the DataFrame in array format