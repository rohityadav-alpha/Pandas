import pandas as pd
import numpy as np

D1=pd.read_csv("D:\\LEARN_PYTHON\\Day-21_Pandas_lib\\03_Pandas_Function\\customers-100.csv")
print(D1)

print(D1.to_numpy()) # .to_numpy() function is used to get the DataFrame in Numpy array format


D2=np.asarray(D1) # .asarray() function is used to get the DataFrame in Numpy array format
print(D2)