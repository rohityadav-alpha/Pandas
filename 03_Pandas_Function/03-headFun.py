import pandas as pd

D1=pd.read_csv("D:\\LEARN_PYTHON\\Day-21_Pandas_lib\\03_Pandas_Function\\customers-100.csv")
print(D1)

print(D1.head(5)) # head() function is used to get first 5 rows of the DataFrame

print(D1[:5]) # This is another way to get first 5 rows of the DataFrame

print(D1[5:10]) # this is how you can get rows data in range (slicing)