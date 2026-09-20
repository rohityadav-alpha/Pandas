import pandas as pd
# to get index values of the csv DataFrame    
D1=pd.read_csv("D:\\LEARN_PYTHON\\Day-21_Pandas_lib\\03_Pandas_Function\\customers-100.csv")
print(D1)
print(D1.index) #.index function is used to get the index values of the DataFrame

print(D1.index.array) # .index.array function is used to get the index values of the DataFrame in array format