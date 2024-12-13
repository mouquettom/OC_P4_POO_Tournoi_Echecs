from random import choice, shuffle
from datetime import datetime, time


class Joueur:

    def __init__(self, prenom, nom, genre, date_naissance):
        self.prenom = prenom
        self.nom = nom
        self.genre = genre
        self.date_naissance = date_naissance
        self.points = 0.0

    def vainqueur_match(self):
        self.points += 1

    def match_nul(self):
        self.points += 0.5

    def __repr__(self):
        return f"{self.prenom} {self.nom} [{self.points} pts]"


class Match:

    def __init__(self, nom, joueurs):
        self.nom = nom
        self.joueurs = joueurs

    def jouer_match(self):
        resultats = choice(["gagnant", "égalité"])
        if resultats == "gagnant":
            gagnant = choice(self.joueurs)
            gagnant.vainqueur_match()
        elif resultats == "égalité":
            for joueur in self.joueurs:
                joueur.match_nul()

    def afficher_resultats_match(self):
        for joueur in self.joueurs:
            print(f" - {joueur.prenom} {joueur.nom} [{joueur.points} pts]")


class Tournoi:

    def __init__(self, nom, lieu, date_debut, date_fin):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.joueurs = []
        self.matchs = []
        self.joueurs_restants = []

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def ajouter_match(self, match):
        self.matchs.append(match)

    def match_making(self):
        if len(self.joueurs_restants) < 2:
            raise ValueError("Il n'y a pas assez de joueurs pour organiser un match.")

        self.joueurs_restants.sort(key=lambda joueur: joueur.points, reverse=True)

        j1, j2 = self.joueurs_restants.pop(0), self.joueurs_restants.pop(0)
        return j1, j2

    def jouer_tour(self):
        self.joueurs_restants = self.joueurs.copy()

        match_count = len(self.joueurs_restants) // 2

        for i in range(match_count):
            j1, j2 = T1.match_making()
            print(f"{j1} va affronter {j2}.")

            M = Match(f"{i + 1}", [j1, j2])
            M.jouer_match()
            M.afficher_resultats_match()

            T1.ajouter_match(M)

    def afficher_classement(self):
        self.joueurs.sort(key=lambda joueur: joueur.points, reverse=True)
        print(f"\nClassement final :")
        print()
        for index, joueur in enumerate(self.joueurs, start=1):
            print(f"{index}. {joueur}")

print()
print("*** TOURNOI D'ECHECS ***")
print()

nom_tournoi = input("Le nom du Tournoi : ")
lieu_tournoi = input("Le lieu du Tournoi : ")
date_debut_tournoi = input("La date de début (JJ/MM/AAAA) : ")
date_debut_obj = datetime.strptime(date_debut_tournoi,"%d/%m/%Y")
date_fin_tournoi = input("La date de fin (JJ/MM/AAAA) : ")
date_fin_obj = datetime.strptime(date_fin_tournoi, "%d/%m/%Y")
T1 = Tournoi(nom_tournoi, lieu_tournoi, date_debut_tournoi, date_fin_tournoi)

print()
while True:
    user_choice = ""

    while user_choice not in ["Y", "N"]:
        user_choice = input("Souhaitez-vous ajouter un joueur (Y/N) ? ")

    if user_choice == "Y":
        prenom_joueur = input("Quel est le prénom du joueur : ")
        nom_joueur = input("Quel est le nom de famille du joueur : ")
        genre_joueur = input("Quel est le genre du joueur (H/F) : ")
        date_naissance = input("Quelle est la date de naissance du joueur (JJ/MM/AAAA) : ")
        date_naissance_obj = datetime.strptime(date_naissance, "%d/%m/%Y")
        joueur = Joueur(prenom_joueur, nom_joueur, genre_joueur, date_naissance_obj)
        T1.ajouter_joueur(joueur)
        print()
    elif user_choice == "N":
        break

shuffle(T1.joueurs)

print()
tour = int(input("Veuillez indiquer le nombre de tours : "))

print("\nLe Tournoi commence :")
print()
for i in range(tour):
    T1.jouer_tour()
    print()

print("\nScores finaux :")
print()
for joueur in T1.joueurs:
    print(joueur)

T1.afficher_classement()