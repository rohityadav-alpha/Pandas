import pandas as pd

D1=pd.read_csv("D:\\LEARN_PYTHON\\Day-21_Pandas_lib\\03_Pandas_Function\\customers-100.csv")
print(D1)

print(D1.tail(10))  # tail() function is used to get last 10 rows of the DataFrame

print(D1[-10:]) # this is another way to get last 10 rows of the DataFrame   

print(D1[-10:-7])   # [last rows : last row to skip] 