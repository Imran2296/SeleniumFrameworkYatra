# arrays need to have similar data types

from array import *

vals = array('i',[3,4,6,7])

#vals = array('u',['a','e','i','o','u']) # 'u' is unicode, we can work with chars as well
print(vals.buffer_info()) #buffer info gives size of array
print(vals.typecode) #it prints type of the code,which is int (i)
vals.reverse() # it reverses the array
print(vals)
for i in range(4):
    print(vals[i])

#array values from user input
arr = array('i',[])
n = int(input("enter len of array"))
for i in range(n):
    x = int(input("enter the values"))
    arr.append(x)

print(arr)

