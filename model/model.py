from datetime import datetime, time
from random import choice, shuffle


class Joueur:

    def __init__(self, prenom, nom, genre):
        self.prenom = prenom
        self.nom = nom
        self.genre = genre
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

    def __init__(self, nom, lieu):
        self.nom = nom
        self.lieu = lieu
        self.joueurs = []
        self.matchs = []
        self.joueurs_restants = []

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def ajouter_match(self, match):
        self.matchs.append(match)

    def match_making(self):
        if len(self.joueurs_restants) < 2:
            raise ValueError("Pas assez de joueurs pour oraniser un match.")

        def tri_points_decroissant(joueurs):
            return -joueurs.points
        #self.joueurs_restants.sort(lambda joueur: -joueur.points)

        self.joueurs_restants.sort(key=tri_points_decroissant)

        j1, j2 = self.joueurs_restants.pop(0), self.joueurs_restants.pop(0)
        return j1,j2

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


print()
print("*** LE TOURNOI D'ECHEC ***")
print()

nom_tournoi = input("Le nom du Tournoi : ")
lieu_tournoi = input("Le lieu du Tournoi : ")
T1 = Tournoi(nom_tournoi, lieu_tournoi)

while True:
    user_choice = ""

    while user_choice not in ["Y", "N"]:
        user_choice = input("Voulez-vous ajouter un joueur ? ")

    if user_choice == "Y":
        prenom = input("Le prénom du joueur ? ")
        nom = input("Le nom du joueur ? ")
        genre = input("Le genre du joueur (H/F) ? ")
        joueur = Joueur(prenom, nom, genre)
        T1.ajouter_joueur(joueur)
    else:
        break

shuffle(T1.joueurs)

tour = int(input("Veuillez indiquer le nombre de tours ? "))
for i in range(tour):
    T1.jouer_tour()
    print()

print(f"\nScores finaux :")
for joueur in T1.joueurs:
    print(joueur)