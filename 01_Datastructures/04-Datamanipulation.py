import pandas as pd 

# Insert data in DataFrame using .insert() method
table={"A":[2,4,3,7,3],"B":[7,9,5,1,6]}
var=pd.DataFrame(table)
print(var)

print()

var.insert(2,"C",var["A"]) #(position of the column , name of the column , values to insert into tha column )
print(var)

print()

var.insert(3,"D",var["A"]+var["B"])
print(var)

print()

ndata=[57,78,98,987,90]
var.insert(4,"E",ndata)
print(var)

print()

# another way to insert values
var["F"]=var["B"]+var["C"]
var["F"]=var["B"][:3]+var["C"][:3]
print(var)

print()


# Delete data from DataFrame using .pop() and del method
var.pop("B")
print(var)

print()

del var["F"]
print(var)