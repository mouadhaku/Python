# Tri Par Selection :

list = [1, 6, 9, 0, 3, 4, 8, 2, 5, 7]
def tri_selection(list):
    for i in range(len(list) - 1):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list

# Tri a Bulle (Bubble Sort) :

def tri_bulle(list):
    permut = True
    while permut:
        permut = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                permut = True
    return list

# Tri Par Insertion

def tri_insertion(list):
    for i in range(1, len(list)):
        cle = list[i]
        j = i - 1
        while j >= 0 and cle < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = cle
    return list



print(f"Main List         : {list}")
print(f"Tri Par Selection : {tri_selection(list)}")
print(f"Tri a Bulle       : {tri_bulle(list)}")
print(f"Tri a Bulle       : {tri_insertion(list)}")

# Output :
# Main List         : [1, 6, 9, 0, 3, 4, 8, 2, 5, 7]
# Tri Par Selection : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Tri a Bulle       : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Tri a Bulle       : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]