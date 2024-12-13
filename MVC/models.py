from random import choice

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