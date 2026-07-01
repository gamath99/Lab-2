"""
Match coin game
Gama MATHURIN
This files runs the game. It creates the player objects andmanages thegame loop and rules.
Import player to be able to use the function from tis file 
06/30/2026
"""


from player import Player

def main():

    #Create the 2 players
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("---coin Match Game---")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

    selection = input("\nDo you want to toss the coins? (y/n): ")

    while selection.lower() == "y":

        #Challenge: game over statement if the player wallet reach zero, no coins. 
        if player1.get_wallet() == 0 or player2.get_wallet() == 0:
            break

        print("\nTossing...")

        # Toss of the coin by each player. 
        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        #Identify the winner

        if side1 == side2:
            print("...It's a Match! Player 1 wins a coin.")
            player1.win_coin()
            player2.lose_coin()

        else:
            print("...No Match! Player 2 wins a coin.")
            player2.win_coin()
            player1.lose_coin()

        print()
        print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

        #Determine when the game is over
        if player1.get_wallet() == 0:
            print("\nPlayer 1 has no coins left!")
            break

        selection = input("\nDo you want to toss the coins? (y/n): ")

    #Final score 
    print("\n --- Final score ---")
    print(f"{player1.get_name()}: {player1.get_wallet()}")
    print(f"{player2.get_name()}: {player2.get_wallet()}")

    if player1.get_wallet() > player2.get_wallet():
        print(f"{player1.get_name()} wins the game!")

    else: 
        print("It's a draw!")

main()