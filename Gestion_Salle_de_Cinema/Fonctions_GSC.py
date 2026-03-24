def print_tableaux(tableaux):
    for ligne in tableaux:
            affichage = "" 
            for casse in ligne:
                affichage += casse + " "
            print(affichage)

def create_tableaux(tableaux, nbr_ligne, nbr_colone):
    for i in range(nbr_ligne):
        ligne = []
        for i in range(nbr_colone):
            ligne.append("□")#■
        tableaux.append(ligne)
    i