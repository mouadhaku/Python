#########################################################

# Code :
e1 = {1,3,5,7}
print("le type de e1 est : ", type(e1))
print("les éléments de e1 sont : ", e1)
e2 = {"Said", 1.79, 30 }
print("e2 : ",e2)
# Output :
le type de e1 est :  <class 'set'>
les éléments de e1 sont :  {1, 3, 5, 7}
e2 :  {1.79, 'Said', 30}

#########################################################

# Code :
# créer un ensemble à partir d'une chaîne
e1 = set("123abc")
print("e1 : ", e1)
# créer un ensemble à partir d'une liste
e2 = set(['Khalid', 'Jarmouni', 'Casa', 32, 1.78])
print("e2 : ", e2)
# créer un ensemble à partir d'un tuple
e3 = set(("Meknes", "Marrakech", "Essaouira"))
print("e3 : ", e3)
# Output :
e1 :  {'a', '2', 'b', '3', 'c', '1'}
e2 :  {32, 1.78, 'Khalid', 'Jarmouni', 'Casa'}
e3 :  {'Marrakech', 'Essaouira', 'Meknes'}

#########################################################

# Code :
e = {1,3}
e.add(5)
print("e : ", e)
# Output :
e :  {1, 3, 5}

#########################################################

# Code :
e.update([9,4,7])
print("e : ", e)
# Output :
e :  {1, 3, 4, 7, 9}

#########################################################

# Code :
e.update([50,51], {100,200})
print("e : ", e)
# Output :
e :  {1, 3, 4, 100, 7, 200, 9, 50, 51}

#########################################################

# Code :
e = {1, 3, 6, 7}
e.discard(3)
print("e : ", e)
# Output :
e :  {1, 6, 7}

#########################################################

# Code :
e.remove(7)
print("e : ", e)
# Output :
e :  {1, 3, 6}

#########################################################

# Code :
e.discard(9)
print("e : ", e)
# Output :
e :  {1, 3, 6, 7}

#########################################################

# Code :
e.remove(9)
print("e : ", e)
# Output :
KeyError: 9

#########################################################

# Code :
e = {2, 4, 90, 100, 30, 32, 1}
val=e.pop()
print("val : ", val)
print("e : ", e)
# Output :
val :  32
e :  {1, 2, 100, 4, 90, 30}

#########################################################

# Code :
e.clear(); print("e : ", e)
# Output :
e :  set()

#########################################################

# Code :
A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
B = {1, 2, 3, 20, 34}
C = A.union(B)
print("Union : ", C)
# Output :
Union :  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 34, 20}

#########################################################

# Code :
A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
B = {1, 2, 3, 20, 34}
C = A.intersection(B)
print("Intersection : ", C)
# Output :
Intersection :  {1, 2, 3}

#########################################################

# Code :
A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
B = {1, 2, 3, 20, 34}
C = A.difference(B)
print("A - B : ", C)
# Output :
A - B :  {4, 5, 6, 7, 8, 9, 10}

#########################################################