from Deck import Deck
import random
from tabulate import tabulate
import pyfiglet

"""
@class Pyfliglet()
Affichage du text<Jeu President -Trou du Coup-> avec <<ASCII art fonts>>
"""


class Pyfliglet():
    def pyfliglet(self):
        GAME = pyfiglet.figlet_format("Jeu President -Trou  du  Cul-")
        print(GAME)


class Player(Deck):

    def __int__(self):
        super().__init__(self)

    score = []
    nb_run = 0
    MAX_PLAYER = 6
    MIN_PLAYER = 3
    nb_player = 0
    NB_CARD = 52
    names = []
    hands = []
    addPlayer = True

    """
    @name_player()
    Système d'inscription de joueurs en entrant le nom
    pas de systeme de vérification de valeur entrée par un joueur 
    """

    def name_player(self):
        while ((self.nb_player < self.MAX_PLAYER) and (self.addPlayer == True)):
            """
            Pour une version avec choix auto des noms mais, problème de bug si on dépasse les 3 joueurs..
            
            ia = ["Macron", "Trump", "Poutine", "Jinping", "Kim Jong-Il", "Zelensky"]
            name = random.choice(ia)
            
            """
            name = input("Entrer your name : ")
            if name == "":
                print('pas de valeur entrée : ')
                break

            self.names.append(name)
            self.nb_player += 1

            if self.nb_player >= self.MIN_PLAYER and self.nb_player < self.MAX_PLAYER:
                print(f" Vous êtes : {str(self.nb_player)} joueurs !! vous pouvez commencez une partie ")
                self.choice = input(" oui : pour jouer | non : pour ajouter un joueur : ")

                if self.choice == "oui":
                    print("let's play")
                    self.addPlayer = False

                    break

            if (self.nb_player == (self.MAX_PLAYER)):
                print("la partie peut commencer")
                print(self.nb_player)

    """
    @hand()
    Cette fonction  qui permet de distribuer les cartes selon le nombre
     de joueurs inscrits
    """

    def hand(self):
        nb_card_by_player = self.NB_CARD // self.nb_player

        random_carte = Deck().get_element()

        while self.NB_CARD >= nb_card_by_player * self.nb_player:

            for player in range(self.nb_player):
                hand_per_player = []
                for col in range(nb_card_by_player):
                    hand_per_player.append(random_carte[self.NB_CARD - 1])
                    self.NB_CARD -= 1
                self.hands.append(hand_per_player)

            for hand in self.hands:
                if self.NB_CARD > 0:
                    hand.append(random_carte[self.NB_CARD - 1])
                    self.NB_CARD -= 1

    """
    Méthode pour fusion les deux listes qui contiennent les noms des joueurs et leur cartes
    pour avoir une formule:
     example => {"player1" :[cards],"player2" :[cards]}

    """

    def player_cards(self):
        player_name = self.names
        player_hands = self.hands
        for player in player_hands:
            player.sort(key=lambda x: x[0])
        dict_hand_and_name = dict(zip(player_name, player_hands))
        return dict_hand_and_name

    def partie(self):

        chosen_card = []
        player_playing = 0
        cards_of_player = self.player_cards()
        for name_player, cards in enumerate(cards_of_player):
            print(f" card of players {cards} ===>{cards_of_player[cards]}")
        nb_cards_parts = 52

        while nb_cards_parts > 0:
            first_player = self.names[0]
            nb_winner = 0
            save_names_delete = []

            print(f" Numero de tour: {self.nb_run}")
            print("*" * 80)

            while (player_playing < self.nb_player):

                if player_playing == 0:
                    card_of_first_player = cards_of_player[first_player]
                    print(f"Joueur: {first_player}")
                    if len(card_of_first_player) > 0:

                        chosen_card = random.choice(card_of_first_player)

                        chosen_card_value = chosen_card[0]

                        print(f"Carte choisie {chosen_card}")
                        cards_of_player[first_player].remove(chosen_card)

                        if len(card_of_first_player) == 0:

                            save_names_delete.append(self.names[0])
                            self.score.append([first_player, self.nb_player - 1])
                            nb_winner += 1

                        nb_cards_parts -= 1
                        print(f"Cartes restantes {card_of_first_player}")
                    else:
                        print('joueur 0: je nai plus de carte à jouer')

                    player_playing += 1
                else:

                    next_player = self.names[player_playing]
                    card_of_current_player = cards_of_player[next_player]
                    if len(card_of_current_player) > 0:
                        i = 0
                        find = False

                        while i < (len(card_of_current_player)) and find == False:
                            if (card_of_current_player[i][0] >= chosen_card_value):

                                if (card_of_current_player[i][0] == chosen_card_value):
                                    print(f'jai une carte de la meme valeur{card_of_current_player[i]}')
                                if (card_of_current_player[i][0] > chosen_card_value):
                                    chosen_card = card_of_current_player[i]
                                    chosen_card_value = card_of_current_player[i][0]
                                    print(f'jai une carte superieure{chosen_card}')

                                find = True
                                cards_of_player[next_player].remove(card_of_current_player[i])
                                if len(card_of_current_player) == 0:
                                    save_names_delete.append(self.names[player_playing])
                                    nb_winner += 1
                                    self.score.append([next_player, self.nb_player - nb_winner])

                                nb_cards_parts -= 1

                            i = i + 1

                        print(f"Cartes restantes {player_playing}{card_of_current_player}")
                    else:
                        print(f"joueur pas de carte à jouer  ")
                    player_playing += 1
                    print(f"nombre de joueur : {player_playing}")
            self.nb_run += 1
            if nb_winner > 0:
                self.nb_player = self.nb_player - nb_winner
                for rm_name in save_names_delete:
                    self.names.remove(save_names_delete[save_names_delete.index(rm_name)])

            player_playing = 0

        print('Fin de la partie')
        print(f"Tableau des scores : {self.score}")
        point_all_players=len(self.point)
        for score_data in self.point:

            if score_data[1] == point_all_players-1:
                score_data.append('Président')

            elif score_data[1]==point_all_players-2:

                score_data.append('vice-président')
            else:
                score_data.append('trou du cul')

            print(tabulate([["Player", "Point", "Titre"], score_data], tablefmt="github"))


decoration = Pyfliglet()
decoration.pyfliglet()

play = Player()
play.name_player()
play.hand()
play.partie()
print(10 * "*")
