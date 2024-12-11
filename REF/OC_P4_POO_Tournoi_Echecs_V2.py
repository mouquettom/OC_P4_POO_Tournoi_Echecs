from random import shuffle, choice
from datetime import datetime
import json


class Joueur:

    def __init__(self, prenom, nom, genre, date_naissance):
        #self.id = id
        self.prenom = prenom
        self.nom = nom
        self.genre = genre
        self.date_naissance = date_naissance
        self.points = 0.0

    def ajouter_point(self):
        self.points += 1.0

    def __repr__(self):
        return f"{self.prenom} {self.nom} [{self.points} pts]"


class Match:

    def __init__(self, nom, joueurs):
        self.nom = nom
        #self.heure_debut = heure_debut
        #self.heure_fin = heure_fin
        self.joueurs = joueurs
        self.resultat = None  # Indique le résultat du match (gagnant ou nul)

    def jouer_match(self):
        # Décider s'il y a un gagnant ou une égalité
        resultat = choice(["gagnant", "egalite"])
        if resultat == "gagnant":
            gagnant = choice(self.joueurs)
            gagnant.ajouter_point()
            self.resultat = f"Gagnant : {gagnant.prenom} {gagnant.nom}"
        else:
            # Cas d'égalité
            for joueur in self.joueurs:
                joueur.points += 0.5
            self.resultat = "Match nul"

    def afficher_resultat(self):
        for joueur in self.joueurs:
            print(f" - {joueur.prenom} {joueur.nom} [{joueur.points}]")


class Tournoi:

    def __init__(self, nom, lieu, description=""):
        self.nom = nom
        self.lieu = lieu
        self.description = description
        self.joueurs = []
        self.matchs = []
        self.joueurs_restants = []

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def ajouter_match(self, match):
        self.matchs.append(match)

    def match_making(self):
        # Vérifie qu'il y a suffisamment de joueurs restants
        if len(self.joueurs_restants) < 2:
            raise ValueError("Pas assez de joueurs restants pour organiser un match.")

        def tri_points_decroissant(joueur):
            return -joueur.points

        self.joueurs_restants.sort(key=tri_points_decroissant)

        # Prend les deux premiers joueurs restants
        j1, j2 = self.joueurs_restants.pop(0), self.joueurs_restants.pop(0)
        return j1, j2

    def jouer_tour(self):
        self.joueurs_restants = T1.joueurs.copy()
        # Organisation des matchs
        match_count = len(self.joueurs_restants) // 2
        for i in range(match_count):
            try:
                # Sélectionner deux joueurs restants
                j1, j2 = T1.match_making()

                # Créer un match entre ces deux joueurs
                M = Match(f"Match {i + 1}", [j1, j2])
                print(f"{j1} va jouer contre {j2}")

                # Jouer le match
                M.jouer_match()
                M.afficher_resultat()

                # Ajouter le match au tournoi
                T1.ajouter_match(M)

            except ValueError as e:
                print(f"Erreur : {e}")
                break


nom_tournoi = input("Nom du Tournoi : ")
lieu_tournoi = input("Lieu du Tournoi : ")
T1 = Tournoi(nom_tournoi, lieu_tournoi)

while True:
    user_choice = ""

    while user_choice not in ["Y", "N"]:
        user_choice = input("Souhaitez-vous ajouter un nouveau joueur (Y/N) ? ")

    if user_choice == "Y":
        prenom = input("Veuillez saisir le prénom du joueur : ")
        nom = input("Veuillez saisir le nom de famille du joueur : ")
        genre = input("Veuillez saisir le genre du joueur (H/F) : ")

        # Demander à l'utilisateur de saisir une date
        date_naissance = input("Veuillez entrer une date (format JJ/MM/AAAA) : ")

        # Valider et convertir la saisie
        try:
            date_obj = datetime.strptime(date_naissance, "%d/%m/%Y")
            print(f"Vous avez saisi la date : {date_obj.strftime('%d %B %Y')}")
        except ValueError:
            print("Le format de la date est invalide. Veuillez réessayer.")

        joueur = Joueur(prenom, nom, genre, date_naissance)
        T1.ajouter_joueur(joueur)

    elif user_choice == "N":
        break
    else:
        continue

shuffle(T1.joueurs)

tour = int(input("Veuillez saisir le nombre de tours : "))
for i in range(tour):
    T1.jouer_tour()
    print()

print(f"\nScores finaux :")
for joueur in T1.joueurs:
    print(joueur)