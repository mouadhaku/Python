list_dict = [{ "Nom" : "Said", "Prenom" : "Jarmouni", "Age" : 18, "Taille": 1.85 },
{ "Nom" : "Khalid", "Prenom" : "Khaldi", "Age" : 19, "Taille": 1.75 },
{ "Nom" : "Sara", "Prenom" : "Montassir", "Age" : 17, "Taille": 1.65 },
{ "Nom" : "Mohamed", "Prenom" : "Slimani", "Age" : 20, "Taille": 1.6 },
{ "Nom" : "Khadija", "Prenom" : "Jarmouni", "Age" : 21, "Taille": 1.75 }]

# Question 1 : ######################################################################
# Code :
def get_nom(D1) :
    return D1["Nom"]
L1 = sorted(list_dict, key = get_nom)
print(L1)
# Output :
[{'Nom': 'Khadija', 'Prenom': 'Jarmouni', 'Age': 21, 'Taille': 1.75}, 
{'Nom': 'Khalid', 'Prenom': 'Khaldi', 'Age': 19, 'Taille': 1.75}, 
{'Nom': 'Mohamed', 'Prenom': 'Slimani', 'Age': 20, 'Taille': 1.6}, 
{'Nom': 'Said', 'Prenom': 'Jarmouni', 'Age': 18, 'Taille': 1.85}, 
{'Nom': 'Sara', 'Prenom': 'Montassir', 'Age': 17, 'Taille': 1.65}]

# Question 1 : ######################################################################
# Code :
L2 = sorted(list_dict, key = lambda D1 : D1["Age"])
print(L2)
# Output :
[{'Nom': 'Sara', 'Prenom': 'Montassir', 'Age': 17, 'Taille': 1.65}, 
{'Nom': 'Said', 'Prenom': 'Jarmouni', 'Age': 18, 'Taille': 1.85}, 
{'Nom': 'Khalid', 'Prenom': 'Khaldi', 'Age': 19, 'Taille': 1.75}, 
{'Nom': 'Mohamed', 'Prenom': 'Slimani', 'Age': 20, 'Taille': 1.6}, 
{'Nom': 'Khadija', 'Prenom': 'Jarmouni', 'Age': 21, 'Taille': 1.75}]
