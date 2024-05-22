students = {'john' : ['python', 'java', 'javascript' ], 'bob':['spring', 'drf'], 'jim':['js', 'node', 'react']}
keys = students.keys()
for eachKey in keys:
     print("Courses taken by", eachKey, "are: ")
     for eachCourse in students[eachKey]:
            print(eachCourse)



list = ['India', 'USA', 'Europe']
list.append('UAE')
del list[1]
list.insert(2, 'France')
print(list)

set = {'Mexico', 'Paris', 'Austria'}
set.add('Ibiza')
set.remove('Mexico')
set.update({'China'})
print(set)
