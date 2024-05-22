s=" YOU are awesome "
print(s)

s1 = """
My name is Ambica
I love to learn programming
Python is interesting
"""
print(s1)

# Indexing = Position for the character in a string
print(s[0])

# String repeation
print(s*2)

#length = Gives the length of the string
print(len(s1))

#Slicing a String
print(s[0:5]) # Does not include the element at the end so, 5 is not included. It prints 0-4
print(s[0:]) #Whole String
print(s[:8]) #Starts at 0 and prints 8 chars
print(s[-3:-1]) #-1: the last element which wont be included. -2 & -3 will be printed.
print(s[0:9:2]) # 2 here is the step value. It prints the alternate numbers.
print(s[-1:0:-2])
print("look here")

#Print the whole string in reverse
print(len(s))
print(s[15::-1]) #Reverse Order
print(s[::-1]) #Reverse String

# Strip spaces
print(s.strip())
print(s.rstrip())
print(s.lstrip())

print(s.find("awe",0,len(s))) #gives the start of the char you are searching.
print(s.count("o")) #counts the no.of occurences of the given sub
print(s.replace("awesome","super")) #Replaces the String

print(s.upper()) #UPPERCASE
print(s.lower()) #lowercase
print(s.split()) #Splits the String
print(s.title())




