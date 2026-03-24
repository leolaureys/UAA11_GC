

def print_tableaux(tableaux):
    for ligne in tableaux:
            affichage = "" 
            for casse in ligne:
                affichage += f"{casse:<3}"
            print(affichage)

def create_tableaux(tableaux, nbr_ligne, nbr_colone):
    
    nbr_ligne = int(input("\nChoisiser le nombre de rangée ===> "))
    nbr_colone = int(input("\nChoisiser le nombre de colonne ===> "))

    nbr_ligne += 1
    nbr_colone += 1

    for i in range(nbr_ligne):
        ligne = []
        if i == 0:
            for j in range(nbr_colone):
                ligne.append(f"{j}")
            tableaux.append(ligne)
        else:
            for j in range(nbr_colone):
                if j == 0:
                    lettre = chr(64 + i)
                    ligne.append(f"{lettre}")
                else:
                    ligne.append("□")#■
            tableaux.append(ligne)
    tableaux[0][0] = " "

def reserver_place():
    ligne_p = input("\nChoisiser la rangée (A, B, C, ...) ===> ")
    colone_P = int(input("\nChoisiser le nombre de colonne ===> "))   