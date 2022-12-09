# Jeu_Trou_Du_Cul
Projet de groupe pour le projet de jeu de carte du trou du cul


# Règle du jeu sur 52 Cartes
- 3 à 6 joueurs, toutes les cartes doivent être distribuer entre les joueurs
- Exemple sur 4 joueurs, le 1er à se débarrasser de toute ses cartes est le président, le 2e vice président, l'avant dernier vice trou du cul et le dernier trou du cul
- Le 2 est la carte supérieur à l'as/1
- Le dernier joueur a avoir posé la plus grosse carte, joue le 1er au prochain tour donc c'est lui qui pose la 1ere carte sur la table
- Le 1er qui joue, peut jouer 1, 2, 3 ou 4 même cartes, les autres doivent suivre le même nombre de carte
( fonctionnalité en plus possible plus tard )

---------------------------------------------------------------------------------------------

Manche = plusieurs parties tant que les joueurs n'ont pas finis toute leurs mains.

# Fonctionnalités
- IA = random
- Distribution = random
- Boucle rejouer = oui, non ( quitter jeu si non)
- Classement des cartes automatique, du plus grand au plus petit dans la main du joueur
- Demander le prénom du joueur, prénom random pour IA pioché dans une liste.
- Sens horaire, le joueur à gauche de celui qui a jouer joue.
- Score ?

# Logique
- Dans une boucle, tant que les joueurs n'ont pas jouer toute leurs cartes la manche n'est pas fini
- Si le 1er joueur joue 1 à 4 cartes alors les autres doivent jouer le même nombre.
- Si le dernier joueur a posé la plus grosse carte alors il joue en 1er au prochain tour.
- Impossible de jouer une carte inférieur à celui posé.
- Impossible de jouer un nombre de carte inférieur et supérieur au nombre jouer ( en rapport avec le 1er SI de la logique )
- Passe automatique Si un joueur n'a pas de carte supérieur à celui jouer ou = au nombre de carte jouer
- Si joueur passe alors il attend fin de la partie.
- Le dernier à avoir jouer le 2 gagne la partie immédiatement et commence en 1er.
- Félicité le trou du cul.
