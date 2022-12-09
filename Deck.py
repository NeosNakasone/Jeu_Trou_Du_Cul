import random


# from Player import Player

class Deck():

    def __init__(self):
        pass

    # liste des carts dans 2 tableaux

    symbol_of_cards = ["♥", "♦", "♣", "♠"]
    cards_type = ["2", "AS", "ROI", "DAME", "VALET", "10", "9", "8", "7", "6", "5", "4", "3"]

    value = 13
    element = []

    def get_element(self):
        for card in self.cards_type:
            for symbol in self.symbol_of_cards:
                self.element.append([self.value, card + symbol])
            self.value = self.value - 1
        shuffled_element = random.sample(self.element, len(self.element))
        return shuffled_element

    """
       def compare_card(self,card,list):
           if card in list:
               card_index = list.index(card)
               return card_index
           else:
               for one_card in list:
                   if one_card ==
           """

    # methode pour melanger les carte  retourner par le methode get_element
    def shuffle(self):
        return random.sample(self.get_element(), len(self.get_element()))

    # nb_carte = 52 # TODO CHERCHER LE NOMBRE DE CARTE
    # nb_player = Player().nb_players() # TODO RECUPERER LE NOMBRE DE JOUEURS