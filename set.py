s = {10,20,30,"xyz",10,20} #Set does not allow duplicates
print(s,type(s))

s.update({10,20,30,"xyz",40,50})
print(s)   #Indexing, Slicing and repetition cannot be done on the SET

s.remove("xyz")
print(s)

f=frozenset(s) #Cannot perform any operations. All we can do is navigate through the frozenset and retrieve the elements.
f.update({0})