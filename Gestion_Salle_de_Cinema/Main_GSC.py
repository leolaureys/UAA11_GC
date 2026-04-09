import Fonctions_GSC as F_GSC
import time

salle_cinema = []

nbr_ligne = 0                                                                       
nbr_colone = 0

continuer_code = True

choix = 6

print("\nLancement Du Programme !\n")
time.sleep(2.5)
print("\nInitialisation De La Salle !\n\n")
time.sleep(1.5)
F_GSC.create_tableaux(salle_cinema, nbr_ligne, nbr_colone)

while continuer_code == True:

    F_GSC.print_menu()
    choix = int(input("\n=====> "))

    if choix == 1:
        F_GSC.print_tableaux(salle_cinema)
    elif choix == 2:
        F_GSC.reserver_place(salle_cinema)
    elif choix == 3:
        F_GSC.delete_reservation(salle_cinema)
    elif choix == 4:
        F_GSC.place_disponible(salle_cinema)
    elif choix == 5:
        F_GSC.compter_place(salle_cinema)
    elif choix == 6:
        salle_cinema = []
        F_GSC.create_tableaux(salle_cinema, nbr_ligne, nbr_colone)
    elif choix == 7:
        continuer_code = False
        print("Au revoir !")
    else:
        print("Choix non-valide !")