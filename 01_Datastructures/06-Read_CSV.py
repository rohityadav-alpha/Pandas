import pandas as pd

# Read csv file 
file1=pd.read_csv("D:\\LEARN_PYTHON\\Day-21_Pandas_lib\\basic-data.csv")
print(file1)

# if you want some specific rows - using nrows parameter
file1=pd.read_csv("D:\\LEARN_PYTHON\\Day-21_Pandas_lib\\basic-data.csv",nrows=1)
print(file1)

# if you want some specific columns - using usecols parameter   
file1=pd.read_csv("D:\\LEARN_PYTHON\\Day-21_Pandas_lib\\basic-data.csv",usecols=["Name"])
print(file1)

# if you want some specific columns - using usecols parameter
file1=pd.read_csv("D:\\LEARN_PYTHON\\Day-21_Pandas_lib\\basic-data.csv",usecols=[1,3])
print(file1)

# if you want to skip specific rows - using skiprows parameter
file1=pd.read_csv("D:\\LEARN_PYTHON\\Day-21_Pandas_lib\\basic-data.csv",skiprows=[3,5])
print(file1)

# if you want to set a specific column as index - using index_col parameter
file1=pd.read_csv("D:\\LEARN_PYTHON\\Day-21_Pandas_lib\\basic-data.csv",index_col="ID")
print(file1)