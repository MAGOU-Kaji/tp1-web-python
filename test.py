

import numpy as np

tableau = np.array([3, 56, 7, 2])
print(tableau)
print("Somme :", np.sum(tableau))
print("Moyenne :", np.mean(tableau))



print("Bonjour !")
fruits = ["pomme", "orange", "banane"]
print("Fruits :", fruits)

fruits.append("mangue")
fruits.insert(2, "ananas")
print(fruits)

nombres = [3, 56, 7, 2]
nombres.sort(reverse=True)
nombres.append(10)
print("Nombres :", nombres)