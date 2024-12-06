#################################

# Code :
a = (5, 6.54, "United States")
type(a)
# Output :
tuple

#################################

# Code :
print(a[1])
# Output :
6.54

#################################

# Code :
a[0] = 13
# Output :
TypeError: 'tuple' object does not support item assignment

#################################

# Code :
print(len(a))
# Output :
3

#################################

# Code :
b = (1, 1.25, ("US", "UK"))
print(b[2][0])
# Output :
US

#################################

# Code :
b = (a, )
print(type(b))
# Output :
tuple

#################################

# Code :
b = 1, 1.25, 'US'
print(type(b))
# Output :
tuple

#################################

# Code :
a, b = (5, 6)
print(a)
print(b)
# Output :
5
6

#################################

# Code :
a = 5
b = 10
a, b = b, a
print(a)
print(b)
# Output :
10
5

#################################

# Code :
a = [1, 2, 3, 4, 5]
print(type(a))
b = tuple(a)
print(type(b))
print(b)
# Output :
list
tuple
(1, 2, 3, 4, 5)

#################################