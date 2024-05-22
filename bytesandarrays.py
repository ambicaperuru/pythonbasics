list=[20,30,40,234]
print(type(list))
b=bytes(list)
print(type(b)) #Cannot add elements into bytes.

b1=bytearray(list)
print(type(b1))
b1[3] = 33
print(b1)