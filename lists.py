#List practice
var = []
random 

print(var)
print(type(var))

var2 = [151, 251, 386, "009"]
print(var2)

var2.append(493) #inplace function doesn't require storing in a variable
print(var2)

#print(dir(var2))

numbers = [0, 2, 4, 6, 8]
print(numbers)
for number in numbers:
    print(number * 2)
    
number_list = list(range(2,10))
print(number_list)

print(number_list[3]) #indexing starts at zero. Should print 5.
