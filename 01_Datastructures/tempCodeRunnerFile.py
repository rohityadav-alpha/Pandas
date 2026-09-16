import pandas as pd
var=pd.DataFrame({"A":[1,5,3,6,7],"B":[7,5,6,3,9]})
var["Agreat20"]=var["A"]>=4
print(var)