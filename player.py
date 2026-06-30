"""
Match coin game
Gama MATHURIN
This class represents a player. A player has a name, has a wallet of coins, 
and has a coin object to toss.
06/30/2026
"""

from coin import Coin

class Player:

    def __init__(self,name):
        """initialize the player."""
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        """Request the player to toss the coin."""
        self.__coin.toss()

    def get_coin_side(self):
        """Reurn the result of the coin toss."""
        return self.__coin.get__sideup()
    
    def win_coin(self):
        """Player gains one coin."""
        self.wallet += 1

    def lose_coin(self):
        """player loses oe coin."""
        self.__wallet -= 1 

    def get_wallet(self):
        """Return the number of coins."""
        return self.__wallet
    
    def get_name(self)
        """Return the name of the player."""
        return self.__name
    
                         
        