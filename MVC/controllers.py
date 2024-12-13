from models import Joueur, Match, Tournoi
from views import TournoiView
from datetime import datetime
from random import shuffle

class TournoiController:
    def __init__(self):
        self.tournoi = None

    def creer_tournoi(self):
        nom, lieu, date_debut, date_fin = TournoiView.demander_info_tournoi()
        date_debut_obj = datetime.strptime(date_debut, "%d/%m/%Y")
        date_fin_obj = datetime.strptime(date_fin, "%d/%m/%Y")
        self.tournoi = Tournoi(nom, lieu, date_debut_obj, date_fin_obj)

    def ajouter_joueurs(self):
        while True:
            choix = ""

            while choix not in ["Y", "N"]:
                choix = input("Souhaitez-vous ajouter un joueur (Y/N) ? ")
            if choix == "Y":
                prenom, nom, genre, date_naissance = TournoiView.demander_info_joueur()
                date_naissance_obj = datetime.strptime(date_naissance, "%d/%m/%Y")
                joueur = Joueur(prenom, nom, genre, date_naissance_obj)
                self.tournoi.ajouter_joueur(joueur)
            else:
                break

    def jouer_tournoi(self, nb_tours):
        shuffle(self.tournoi.joueurs)
        for i in range(nb_tours):
            self.tournoi.joueurs_restants = self.tournoi.joueurs.copy()
            while len(self.tournoi.joueurs_restants) >= 2:
                j1, j2 = self.tournoi.match_making()
                TournoiView.afficher_match(j1, j2)
                match = Match(f"Match {len(self.tournoi.matchs) + 1}", [j1, j2])
                match.jouer_match()
                TournoiView.afficher_resultats_match(match.joueurs)
                self.tournoi.ajouter_match(match)

    def afficher_classement(self):
        self.tournoi.joueurs.sort(key=lambda joueur: joueur.points, reverse=True)
        TournoiView.afficher_classement(self.tournoi.joueurs)