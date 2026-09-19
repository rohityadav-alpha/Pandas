import pandas as pd

# Read csv file 
file1=pd.read_csv("D:\\LEARN_PYTHON\\Day-21_Pandas_lib\\basic-data.csv")
print(file1)

# if you want some specific rows - using nrows parameter
file1=pd.read_csv("D:\\LEARN_PYTHON\\Day-21_Pandas_lib\\basic-data.csv",nrows=1)
print(file1)