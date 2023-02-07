var = {}

print(var)
print(type(var))

var2 = {"fruit": "mango", "juice":"apple", "food":"shrimp scampi"}

print(var2)

for k, v in var2.items():
    print(k, v)

#adding a variable 
var2["drink"] = "pina colada"
print(var2)

#updating a variable 
var2["fruit"] = "orange"
print(var2)

print(list(var2.keys())) 
