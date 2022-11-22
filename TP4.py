liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

# ajouter un element a une liste : append

for i in range(len(liste1)):
    print(i, ":", liste2[i])

# Creer une fonction qui somme deux listes
# [1, 2, 3] + [4, 5, 6] -> [5, 7, 9]

def sommeVecteur(liste1, liste2):
    resultat = []
    for i in range(len(liste1)):
        resultat.append(liste1[i] + liste2[i])
    return resultat

print("somme :", sommeVecteur(liste1, liste2))