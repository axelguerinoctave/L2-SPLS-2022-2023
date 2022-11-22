liste = [2, 3, 1, 7, 5]

print(liste)

print("taille de la liste :", len(liste))
print("premier element :", liste[0])

for elem in liste:
    print("element :", elem)

somme = 0
for elem in liste:
    somme = somme + elem
print("somme :", somme)
print("somme :", sum(liste))

def moyenne(liste):
    somme = 0
    for elem in liste:
        somme = somme + elem
    moyenne = somme / len(liste)
    return moyenne

print("moyenne :", moyenne(liste))