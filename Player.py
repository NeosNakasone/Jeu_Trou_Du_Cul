from Deck import Deck
import random
from tabulate import tabulate

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

    # Récupérer les cartes des deux tableaux qui se trouve dans la class Deck

    # print(f" randomecarddddddddd  ===>{Deck().get_element()}")
    # Melange les carte des deux tableaux => get_element
    # shuffle = Deck().shuffle()

    # Partie du code qui gère l'entrée des joueurs dans la partie

    def name_player(self):
        while ((self.nb_player < self.MAX_PLAYER) and (self.addPlayer == True)):
            name = input("Entrer your name :")
            if name == "":
                print('pas de valeur entrée :')
                break

            self.names.append(name)
            self.nb_player += 1
            if self.nb_player >= self.MIN_PLAYER and self.nb_player < self.MAX_PLAYER:
                print(f" Vous êtes : {str(self.nb_player)} joueurs !! vous pouvez commencez une partie ")
                self.choice = input(" Votre choix : oui ou non : ")

                if self.choice == "oui":
                    print("let's play")
                    self.addPlayer = False

                    break

            if (self.nb_player == (self.MAX_PLAYER)):
                print("la partie peut commencer")
                print(self.nb_player)

    # Partie du code qui distribut les carte selon le nombre de joueurs

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

    # Methode pour fusion les deux listes qui contiennent les noms des joueurs et leur cartes
    # {name:[cards]
    def player_cards(self):
        player_name = self.names
        player_hands = self.hands
        for player in player_hands:
            player.sort(key=lambda x: x[0])
        dict_hand_and_name = dict(zip(player_name, player_hands))
        return dict_hand_and_name

    # TODO le joueur qui commence la partie:

    # premier joueur inscrit , commence !

    def partie(self):

        chosen_card = []
        player_playing = 0
        cards_of_player = self.player_cards()
        for name_player, cards in enumerate(cards_of_player):
            print(f" card of players {cards} ===>{cards_of_player[cards]}")
        nb_cards_parts = 52  # pour qu'on puisse boucler tant qu'il y'a des cartes dans la main des joueur
        # tant qu'il y'a une carte en main
        # while (nb_cards_parts>0 and self.nb_run <16 ):
        while nb_cards_parts > 0:
            first_player = self.names[0]
            nb_winner = 0
            save_names_delete = []

            print(f" Numero de manche:==>{self.nb_run}")
            print("*" * 80)

            # parcourir les players = une manche

            while (player_playing < self.nb_player):
                # PARCOURIR LA MAIN DU PREMIER JOUEUR

                if player_playing == 0:
                    card_of_first_player = cards_of_player[first_player]
                    # !!!!!!!!!!!!!!!!!!!!!!!!faire un system de choix de carte à prpoôser
                    print(f"Joueur==>{first_player}")
                    if len(card_of_first_player) > 0:

                        chosen_card = random.choice(card_of_first_player)

                        chosen_card_value = chosen_card[0]

                        print(f"Carte choisie {chosen_card}")
                        cards_of_player[first_player].remove(chosen_card)

                        # retirer immediatemennt  le player
                        if len(card_of_first_player) == 0:
                            # self.names.remove(self.names[0])
                            save_names_delete.append(self.names[0])
                            self.score.append([first_player, self.nb_player - 1])
                            nb_winner += 1

                        nb_cards_parts -= 1
                        print(f"Cartes restantes {card_of_first_player}")
                    else:
                        print('joueur 0: je nai plus de carte à jouer')

                    player_playing += 1
                else:

                    # PARCOURIR LES MAINS DES AUTRES JOUEURS
                    # TODO  FAIRE LA COMPARAISON  DES CARTES CHOISI PAR LES JOUEURS
                    next_player = self.names[player_playing]
                    card_of_current_player = cards_of_player[next_player]
                    if len(card_of_current_player) > 0:
                        i = 0
                        find = False
                        # parcourir les cartes du current player
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

                                # retirer immediatemennt  le player

                                nb_cards_parts -= 1

                            i = i + 1
                            # si j'atteints la fin du tableau et que que je n'ai rien trouvé, je vais chercher les valeurs supperieurs

                        print(f"Cartes restantes {player_playing}{card_of_current_player}")

                        # TODO  AJOUTER SYSTEME DE SELECTION DE CARTE  DEPUIS
                    else:
                        print(f" joueur pas de carte à jouer  ")
                    player_playing += 1
                    print(f"nombre de joueur {player_playing}")
            self.nb_run += 1
            if nb_winner > 0:
                self.nb_player = self.nb_player - nb_winner
                for rm_name in save_names_delete:
                    self.names.remove(save_names_delete[save_names_delete.index(rm_name)])

            player_playing = 0

        print('Fin de la partie')
        print(f" tableau des scors ====>{self.score}")
        for data in self.score:


            print(tabulate([["player", "Title"], data], headers="firstrow"))

# TODO add_to_hand()  methode pour  ajouter carte à une main suite un manche de jouer
# TODO remove_from_hand() methode pour  supprimer une carte d'une main suite un manche de jouer
# TODO play()

play = Player()
play.name_player()
play.hand()
play.partie()
print(10 * "*")