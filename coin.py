"""
Match coin Game
Gama MATHURIN
This file contain the class that represent a single, tossable coin. 
The result can be either head or tail. 
06/29/2026
"""

#import random to be ale to choose the side

import random

#Create the class coin 
class Coin:

    #assign function to initialize the coin.     
    def __init__(self):
        """Initialize the coin."""
        self.__sideup ="Heads"

    #Assign function to toss the coin randomly with two possibilities. 
    def toss(self):
        """Toss the coin."""
        if random.randint(0,1) == 0:
            self.__sideup = "Heads"
        else: 
            self.__sideup = "Tails"

    #Assign function 
    def get_sideup(self):
        """Return the side facing up"""
        return self.__sideup
    