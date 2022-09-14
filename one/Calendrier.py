print("rentrer nombre de jours dans le mois : ")
nbr_jours_mois = int(input())

print("Entrez le premier jour du mois : 1 pour lundi, 7 pour dimanche")
premier_jour = int(input())
colonne_courante = premier_jour
liste_Jours = "LUN MAR MER JEU VEN SAM DIM "
print(liste_Jours)

nbr_colonne_vides = premier_jour - 1
largeur_colonne = 4
print("" * largeur_colonne * nbr_colonne_vides, end="")

for i in range(nbr_jours_mois) :
  print("{0:3d}".format(i+1),end=" ")
  colonne_courante= colonne_courante + 1
  if colonne_courante == 8 :
    print()
    colonne_courante = 1
