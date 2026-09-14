import pandas as pd 
a=[2,5,6,7]
a1=pd.Series(a,index=[1,2,3,4])
a2=pd.Series(a,index=[1,2])
print(a1+a2)

b1=pd.Series(10,index=[1,2,3,4,5,6])
b2=pd.Series(10,index=[1,2,3,4])
print(b1+b2)