import math

# Ex 1 :

def com_element(list1, list2):
    return list(list1 and list2)

# Ex 2 :

def not_com_element(list1, list2):
    list = []
    for i in list1:
        if i not in list2:
            list.append(i)
    return list

# Ex 3 :

def sym_element(list1, list2):
    list = []
    for i in list1:
        if i not in list2:
            list.append(i)
    for j in list2:
        if j not in list1:
            list.append(j)
    return list

# Ex 4 :

def couple(l):
    list = []
    for m in l:
        for n in l:
            if n + m < 10:
                list.append((n, m))
    return list

# Ex 5 :

Age = [
    19, 17, 21, 18, 19, 19, 22, 23, 
    20, 18, 21, 24, 19, 22, 20, 18,
    22, 21, 19, 20, 19, 23, 21, 18,
    20, 19, 20, 20, 19, 20]

lenghtAge = len(Age)

# Question 1 : La Serie Statistique

Age.sort()
statistique_serie = []
for i in Age:
    (j, n) = (i, Age.count(i))
    if (j, n) not in statistique_serie:
        statistique_serie.append((j, n))

print(f"La serie statistique      : {statistique_serie}")

# Question 2 : Le Moyenne Arithmetique
# Le Moyenne Arithmetique = La somme des produit des effectif / La somme des effictifs

somme1 = 0
for i in range(len(statistique_serie)):
    somme1 += statistique_serie[i][0] * statistique_serie[i][1]
somme2 = 0
moyenne_arth = somme1 / lenghtAge

print(f"Le moyenne arithmetique   : {moyenne_arth}")

# Question 2 : La Frequences
# La Frequences = Efectif /  La somme des efectifs

frequence = []
for i in statistique_serie:
    frequence.append((i[0], round(i[1] / lenghtAge, 2)))

print(f"La serie des frequences   : {frequence}")

# Question 2 : La Variance et L'ecartype
# La Varinace

variance = 0
for i in statistique_serie:
    variance += (i[1] * ((i[0] - moyenne_arth) ** 2)) / lenghtAge

print(f"La Varinace               : {variance}")
# L'ecartype

ecartype = math.sqrt(variance)
print(f"L'ecartype                : {ecartype}")




