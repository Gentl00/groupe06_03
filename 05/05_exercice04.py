# Exercice 4 — Liste de carrés et filtrage
carres = []
for i in range(1, 21):
    carres.append(i ** 2)

print("Tous les carrés :", carres)
print("Carrés > 100 :")
for val in carres:
    if val > 100:
        print(val)
