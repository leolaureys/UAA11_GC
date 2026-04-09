def print_menu():
    print("\n\n|=========================== MENU ============================|")
    print("|                                                             |")
    print("| 1 : afficher la salle                                       |")
    print("| 2 : réservée une place                                      |")
    print("| 3 : annuler une réservation                                 |")
    print("| 4 : vériffier si un place est disponible                    |")
    print("| 5 : compter le nombre de place                              |")
    print("| 6 : inisialitation d'une nouvelle salle                     |")
    print("| 7 : Quitter                                                 |")
    print("|_____________________________________________________________|")


def print_tableaux(tableaux):
    print("\n")
    for ligne in tableaux:
            affichage = "" 
            for case in ligne:
                affichage += f"{case:<3}"
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


def reserver_place(tableaux):
    try:
        ligne_p = input("\nChoisiser la rangée (A, B, C, ...) ===> ")
        ligne_p = ligne_p.lower()
        ligne_p = ord(ligne_p) - 96
        colone_p = int(input("\nChoisiser le nombre de colonne ===> "))   

        if tableaux[ligne_p][colone_p] == "■":

            print("\nPlace déja réservée !")

        elif tableaux[ligne_p][colone_p] == "□":

            tableaux[ligne_p][colone_p] = "■"
            print("\nPlace réservée !")

        else:
            print("\nErreur place invalide !")

    except(ValueError):
        print("\n\nEreur place invalide !")


def delete_reservation(tableaux):
    try:
        ligne_p = input("\nChoisiser la rangée (A, B, C, ...) ===> ")
        ligne_p = ligne_p.lower()
        ligne_p = ord(ligne_p) - 96
        colone_p = int(input("\nChoisiser le nombre de colonne ===> "))   

        if tableaux[ligne_p][colone_p] == "□":

            print("\nPlace non-réservée !")

        elif tableaux[ligne_p][colone_p] == "■":

            tableaux[ligne_p][colone_p] = "□"
            print("\nréservation annuler !")

        else:
            print("\nErreur place invalide !")

    except(ValueError):
        print("\n\nErreur place invalide !")


def place_disponible(tableaux):
    try:
        ligne_p = input("\nChoisiser la rangée (A, B, C, ...) ===> ")
        ligne_p = ligne_p.lower()
        ligne_p = ord(ligne_p) - 96
        colone_p = int(input("\nChoisiser le nombre de colonne ===> "))   

        if tableaux[ligne_p][colone_p] == "□":

            print("\nPlace disponible !")

        elif tableaux[ligne_p][colone_p] == "■":

            print("\nPlace indisponible !")

        else:
            print("\nErreur place invalide !")

    except(ValueError):
        print("\n\nErreur place invalide !")


def compter_place(tableaux):

    p_vide = 0
    p_reserv = 0

    for ligne in tableaux:
            for case in ligne:
                if case == "□":
                    p_vide += 1
                elif case == "■":
                    p_reserv += 1
    print(f"\n\nIl y a {p_vide} place disponible et {p_reserv} place réservée !")