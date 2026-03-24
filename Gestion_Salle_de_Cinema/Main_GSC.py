import Fonctions_GSC as fg

salle_cinema = []

logueur_ligne = 3
logueur_colone = 5

for i in range(1,0,logueur_ligne):
    ligne = []
    for j in range(1,0,logueur_colone):
        ligne.append("#")
        salle_cinema.append(ligne)

for i in salle_cinema:
            to_display = "" 
            for casse in i:
                to_display += casse + " "
            print(to_display)   
