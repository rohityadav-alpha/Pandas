import pandas as pd 

var=pd.DataFrame({"A":[1,5,3,6,7],"B":[7,5,6,3,9]})
print(var)
print("Addition")
var["C"]=var["A"]+var["B"]
print(var)
print("Substraction")
var["C"]=var["A"]-var["B"]
print(var)
print("Multiplication")
var["C"]=var["A"]*var["B"]
print(var)
print("Division")
var["C"]=var["A"]/var["B"]
print(var)


import pandas as pd
var=pd.DataFrame({"A":[1,5,3,6,7],"B":[7,5,6,3,9]})
var["Agreat4"]=var["A"]>=4
var["Bsmall5"]=var["B"]<=5
print(var)