class Game():

    def play_the_game(player1,player2):
        if player1.choice == player2.choice:
            return None
        elif player1.choice == "rock":
            if player2.choice == "scissors":
                return player1
            else:
                return player2
        elif player1.choice == "paper":
            if player2.choice == "rock":
                return player1
            else:
                return player2
        elif player1.choice =="scissors":
            if player2.choice=="paper":
                return player1
            else:
                return player2



