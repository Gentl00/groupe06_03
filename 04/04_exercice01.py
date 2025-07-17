# Exercice 1 — Calculateur d'abonnement cinéma
age = int(input("Âge: "))
statut = input("Statut (étudiant/salarié/retraité) :").lower()

if age < 18:
    tarif = 5
else:
    if 18 <= age <= 25:
        if statut == "étudiant":
            tarif = 6
        elif statut == "salarié":
            tarif = 8
        else:
            tarif = 10
    else:
        if statut == "retraité":
            tarif = 7
        else:
            tarif = 10

print(f"Votre tarif est de {tarif} €.")
