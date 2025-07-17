"""Ce programme est un calculateur de factures"""

montant_ht = float(input("Montant HT (euros) : "))
taux_tva = float(input("Taux de TVA(%) : "))

# conversion en coefficient multiplicateur
taux_coef = taux_tva / 100

# Calcul TTC
montant_ttc = montant_ht * (1 + taux_coef)
print(f"Montant TTC {montant_ttc: .2f} €")