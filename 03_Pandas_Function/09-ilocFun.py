import pandas as pd
import numpy as np

D1=pd.read_csv("D:\\LEARN_PYTHON\\Day-21_Pandas_lib\\03_Pandas_Function\\customers-100.csv")
print(D1)

print(D1.iloc[0,2]) # .iloc[row index, column index] function is used to get the row values of the DataFrame by integer position