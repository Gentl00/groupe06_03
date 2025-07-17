"""Ce programme affiche la somme, la différence
le produit, le quotient, la division et le modulo
de deux nombres fournis ar l'utilisateur"""

# Demander deux nombres
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

# Calculs
somme = a + b
difference = a - b
produit = a * b
quotient = a / b if b != 0 else "Division par zéro"
division_entiere = a // b if b != 0 else "Division par zéro"
reste = a % b if b != 0 else "Division par zéro"

# Affichage des résultats
print(f"sornme : {somme}")
print(f"Différence : {difference}")
print(f"Produit : {produit}")
print(f"Quotient : {quotient}")
print(f"Division entière : {division_entiere}")
print(f"Reste : {reste}")