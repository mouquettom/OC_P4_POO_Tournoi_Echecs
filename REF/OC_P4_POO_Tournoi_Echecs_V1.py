from datetime import time, datetime
from random import shuffle, choice
import json


class Joueur:

    def __init__(self, id, prenom, nom, genre, date_naissance, rang):
        self.id = id
        self.prenom = prenom
        self.nom = nom
        self.genre = genre
        self.date_naissance = date_naissance
        self.rang = rang
        self.points = 0.0

    def ajouter_point(self):
        self.points += 1.0

    def __repr__(self):
        return f"{self.prenom} {self.nom} [{self.points} pts]"


class Match:

    def __init__(self, nom, heure_debut, heure_fin, joueurs):
        self.nom = nom
        self.heure_debut = heure_debut
        self.heure_fin = heure_fin
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

    def __init__(self, nom, lieu, date_debut, date_fin, description=""):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
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
                M = Match(f"Match {i + 1}", heure_debut, heure_fin, [j1, j2])
                print(f"{j1} va jouer contre {j2}")

                # Jouer le match
                M.jouer_match()
                M.afficher_resultat()

                # Ajouter le match au tournoi
                T1.ajouter_match(M)

            except ValueError as e:
                print(f"Erreur : {e}")
                break


# Création des joueurs
joueurs = [
    Joueur("tom256", "Tom", "Mouquet", "Homme", datetime(1996, 7, 29), 1),
    Joueur("nao117", "Nao", "Dovi", "Femme", datetime(1995, 4, 19), 1),
    Joueur("vic318", "Victor", "Bondue", "Homme", datetime(1996, 8, 18), 1),
    Joueur("oph139", "Ophelie", "Trenta", "Femme", datetime(1995, 5, 14), 2),
    Joueur("max479", "Maxime", "Tabard", "Homme", datetime(1990, 12, 24), 2),
    Joueur("jul105", "Jules", "Jung", "Homme", datetime(1994, 6, 11), 2),
]

shuffle(joueurs)

# Création du tournoi
heure_debut = time(15, 30)
heure_fin = time(17, 0)
T1 = Tournoi("Lancement", "Paris", datetime(2024, 7, 18), datetime(2024, 7, 21))
T1.joueurs = joueurs


for tour in range(4):
    T1.jouer_tour()
    print()

# Afficher les scores finaux
print("\nScores finaux :")
for joueur in T1.joueurs:
    print(f"{joueur}")