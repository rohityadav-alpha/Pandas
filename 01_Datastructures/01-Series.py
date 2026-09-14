# DataStructures in pandas 
# pandas has 3 DataStructures 
# 1.series
# 2.Data Frame
# 3.panel 

# 1. Series datastructure
# pandas.Series has parimeter 
# 1.index=[]  for custom indexing
# 2.dtypes=[] for custom datatype change and assign
# 3.name=[] for custom name for the datastructure

import pandas as pd
# series with list
a=[2,5,6,7]
b=pd.Series(a)
print(b)
# index paremeter
c=pd.Series(a,index=[1,2,3,4])
print(c)
# dtype paremeter
d=pd.Series(a,index=["a","b","c","d"],dtype=(float))
print(d)
#name paremeter
e=pd.Series(a,index=["rohit","ashish","vijay","shubham"],dtype=(float),name="Sreies datastructure")
print(e)

print()

# Series with dictionary
dict1={"name":["rohit","ashish","vijay","shubham"],"age":[24,23,21,20],"marks":[67,87,56,98]}
var=pd.Series(dict1)
print(var)

print()

# series with tuple
tu=(3,2,5,"rohit")
nt=pd.Series(tu)
print(nt)
print(nt[3])

print()

# series with set
s={2,5,4,3}
s1=pd.Series(sorted(s))
print(s1)


# Pandas allow nan values
# this works
import pandas as pd 
b1=pd.Series(10,index=[1,2,3,4,5,6])
b2=pd.Series(10,index=[1,2,3,4])
print(b1+b2)
# but this not
a=[2,5,6,7]
a1=pd.Series(a,index=[1,2,3,4])
a2=pd.Series(a,index=[1,2])
print(a1+a2)