#Way of converting string into a sequence of characters using string.

#1. By creating list
s = 'flamboyant'
s_list = list(s)
print(s_list)

#2. By using split function
a = 'honourable person in this world'
b = a.split() #This also creates a list of strings distinguished by a space.
print(b)

#Similar to 2
c = 'crazy-person-of-this-world'
d = c.split('-')
print(d)

#Now joining the list values to form a single string.
e = ['He','is','very','good','person.']
splitter = ' '
f = splitter.join(e)
print(f)