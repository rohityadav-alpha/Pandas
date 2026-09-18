import pandas as pd 

# Insert data in DataFrame 
table={"A":[2,4,3,7,3],"B":[7,9,5,1,6]}
var=pd.DataFrame(table)
print(var)

print()

var.insert(2,"C",var["A"]) #(position of the column , name of the column , values to insert into tha column )
print(var)

print()

