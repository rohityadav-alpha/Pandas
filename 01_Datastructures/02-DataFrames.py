# Dataframe with list
import pandas as pd
a=[3,5,2,55,"rohit"]
a1=pd.DataFrame(a,index=[1,2,3,4,5])
print(a1)


b={"name":["rohit","shubham","kuldeep","ganesh"],"age":[22,23,21,20],"marks":[87,76,53,62]}
b1=pd.DataFrame(b,index=[1,2,3,4])
print(b1)
print()
print(pd.DataFrame(b,index=[1,2,3,4],columns=["name"])) #this returns only single column
print(b1["name"][3]) #this returns single value from the column name and index 3 



dict1={"voval":pd.Series(["a","e","i","o","u"]),"consonent":pd.Series(["b","c","d","f","g"])}
dict2=pd.DataFrame(dict1,index=[0,1,2,3,4,5,6])
print(dict2)