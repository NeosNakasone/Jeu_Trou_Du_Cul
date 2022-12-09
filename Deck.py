import random
class Deck():

    def __init__(self):
        pass

    symbol_of_cards = ["♥", "♦", "♣", "♠"]
    cards_type = ["2", "AS", "ROI", "DAME", "VALET", "10", "9", "8", "7", "6", "5", "4", "3"]

    value = 13
    element = []
    """
    @get_element
     Etape : 1 =>Recupération des données depuis les deux lists symbole_of_cards et cards_type et les fusionner 
     pour façon à obtenir les les 52 cartes du jeu
     Etape : 2 => Melanger les cartes
     
    """
    def get_element(self):
        for card in self.cards_type:
            for symbol in self.symbol_of_cards:
                self.element.append([self.value, card + symbol])
            self.value = self.value - 1
        shuffled_element = random.sample(self.element, len(self.element))
        return shuffled_element


























