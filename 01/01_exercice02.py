"""Création d'une mini fiche produit"""

nom_produit = "Casque Bluetooth"
prix = 150.0
stock = 25
remise = 0.15


prix_final = prix * (1-remise)

print("produit", nom_produit)
print(f"Prix initial : {prix} euros")
print(f"Remisec: {remise * 100}%")
print(f"Prix final : {prix_final:.2f} euros")
print(f"Stock disponible : {stock}")