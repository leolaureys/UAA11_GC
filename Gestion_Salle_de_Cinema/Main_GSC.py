import Fonctions_GSC as F_GSC

salle_cinema = []

nbr_ligne = 0                                                                       
nbr_colone = 0

continuer_code = True

choix = 1

while continuer_code == True:
    try:

        F_GSC.print_menu()

        choix = input("=====> ")

    except(ValueError):
        print("\n\nEreur de Valeur !")