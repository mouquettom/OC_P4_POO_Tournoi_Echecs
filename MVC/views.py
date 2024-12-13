# views.py
class TournoiView:
    @staticmethod
    def afficher_classement(joueurs):
        print("\nClassement final :\n")
        for index, joueur in enumerate(joueurs, start=1):
            print(f"{index}. {joueur}")

    @staticmethod
    def afficher_match(j1, j2):
        print(f"{j1} va affronter {j2}.")

    @staticmethod
    def afficher_resultats_match(joueurs):
        for joueur in joueurs:
            print(f" - {joueur.prenom} {joueur.nom} [{joueur.points} pts]")

    @staticmethod
    def demander_info_tournoi():
        nom = input("Le nom du Tournoi : ")
        lieu = input("Le lieu du Tournoi : ")
        date_debut = input("La date de début (JJ/MM/AAAA) : ")
        date_fin = input("La date de fin (JJ/MM/AAAA) : ")
        return nom, lieu, date_debut, date_fin

    @staticmethod
    def demander_info_joueur():
        prenom = input("Quel est le prénom du joueur : ")
        nom = input("Quel est le nom de famille du joueur : ")
        genre = input("Quel est le genre du joueur (H/F) : ")
        date_naissance = input("Quelle est la date de naissance du joueur (JJ/MM/AAAA) : ")
        return prenom, nom, genre, date_naissance