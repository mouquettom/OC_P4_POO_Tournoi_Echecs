from controllers import TournoiController

if __name__ == "__main__":
    print("\n*** TOURNOI D'ECHECS ***\n")
    controller = TournoiController()
    controller.creer_tournoi()
    controller.ajouter_joueurs()
    nb_tours = int(input("Veuillez indiquer le nombre de tours : "))
    controller.jouer_tournoi(nb_tours)
    controller.afficher_classement()