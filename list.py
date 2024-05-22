list = [10,20,'ambica',-10,30.5]
print(list)
print(len(list)) #Starts from 1
print(list[0:3]) #Slicing
print(list[-3:])
print(list[::-1])
print(list*2) #Repetition
print(list[0]) #Indexing

#Add or Delete by passing value
list.append(40)
list.remove('ambica')
print(list)

#Add or Delete by passing index
del list[1]
print(list)

#list.clear()
#print(list)

print(max(list))
print(min(list))

list.insert(3,99) #Insert wherever you want.
print(list)

list.sort() #Sorts in an Order
print(list)

#list.reverse()

list.sort(reverse=True)
print(list)