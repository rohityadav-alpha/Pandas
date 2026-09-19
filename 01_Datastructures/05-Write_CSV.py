import pandas as pd 

data1=pd.DataFrame({"Even":[2,8,4,6,10],"Odd":[1,9,3,5,7]})
print(data1)

print()


# Creating csv file
data1.to_csv("test.csv")
data1.to_csv("test1.csv",index=False)  #("nameof the csv file" , remove index value from csv file)
data1.to_csv("test2.csv",index=False,header=["E","O"]) #("nameof the csv file" , remove index value , Custom Column name )
