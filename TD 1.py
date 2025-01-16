# Ex 1 :

nom = input("Quel est ton nom ? ")
print(f"Bienvenue {nom}!")

# Ex 2 :

num1 = int(input("Premier numéro  : "))
num2 = int(input("Deuxième numéro : "))
print(f"{num1} + {num2} = {num1 + num2}")

# Ex 3 :

n1 = int(input("Premier numéro  : "))
n2 = int(input("Deuxième numéro : "))

if n1 > n2:
	print(f"Maximum est {n1}")
elif n1 < n2:
	print(f"Maximun est {n2}")
else:
	print(f"{n1} et {n1} sont egaux")


#Ex 4 :

age = int(input("Quel âge as-tu ? "))

if age >= 18:
	print("Majeur")
else:
	print("Mineur")

# Ex 5 :

moyen = float(input("Quel est votre moyen ? "))

if moyen < 10:
	print("Insuffisant")
elif moyen < 12:
	print("Passable")
elif moyen < 14:
	print("Assez Bient")
elif moyen < 16:
	print("Bien")
else:
	print("Tres bien")

# Ex 6 :

num = int(input("Donner une nombre entier : "))

if num % 2 == 0:
	print(f"Le nombre {num} est pair")
else:
	print(f"Le nombre {num} est impair")

# Ex 7 :

for i in range(1, 101):
	print(i)

# Ex 8 :

n = int(input("Donner une nombre : "))

for i in range(1, 11):
	print(f"{n} x {i} = {i * n}")

# Ex 9 :

number = int(input("Donner une nombre : "))

somme = 0
for i in range(1, number + 1):
	somme += 1
print(somme)

# Ex 10 :

div = int(input("Donner une nombre : "))

for i in range(1, div):
	if div % i == 0:
		print(f"{i} est un divisuer de {div}")

# Ex 11 :

parfait = int(input("Donner une nombre : "))

somme = 0
for i in range(1, parfait):
	if parfait % i == 0:
		somme += i

if somme == parfait:
	print(f"{parfait} est un nombre parfait")
else:
	print(f"{parfait} n'est pas un nombre parfait")

# Ex 12 :

premier = int(input("Donner une nombre entier : "))

bool = True
for i in range(2, premier):
	if premier % i == 0:
		bool = False

if bool and premier > 1:
	print(f"Le nombre {premier} est premier")
else:
	print(f"Le nombre {premier} n'est pas premier")
