def tic_tac_toe():
    # Enter names of players that will be playing the game
    player1 = input("Enter name for player 1: ")
    player2 = input("Enter name for player 2: ")

    # initialize variables
    choices = []
    checkturns = []
    for x in range(0, 9):
        choices.append(str(x + 1))
    playerOneTurn = True  # the game starts with player 1's turn
    winner = False  # boolean to check if anyone wins the game

    # Create the board
    def printBoard():
        print(' ' + choices[0] + ' ' + '|' + ' ' + choices[1] + ' ' + '|' + ' ' + choices[2] + ' ')
        print('-----------')
        print(' ' + choices[3] + ' ' + '|' + ' ' + choices[4] + ' ' + '|' + ' ' + choices[5] + ' ')
        print('-----------')
        print(' ' + choices[6] + ' ' + '|' + ' ' + choices[7] + ' ' + '|' + ' ' + choices[8] + ' ')

    # while there is no winner, run the printboard function
    while not winner:
        printBoard()

        # if 9 turns has already passed with no winner, no one has won the game
        if len(checkturns) == 9 and winner == False:
            print("Both players have lost!")
            break

        # if its player 1's turn, place X, if not place O for player 2
        if playerOneTurn:
            print(f"{player1},Choose a box to place an X into")
        else:
            print(f"{player2},Choose a box to place an O into")

        # try recording the players input with ">>" and append the X or O into the chosen number
        try:
            choice = int(input(">> "))
            checkturns.append(choice)

        # if there isnt a valid field entered, throw exception
        except:
            print("please enter a valid field")
            continue

        # if an X or an O is placed on a field where there is already an X or an O, say its an illegal move
        if choices[choice - 1] == 'X' or choices[choice - 1] == 'O':
            print("illegal move, plase try again")
            continue

        # Use X for player1 and O for player 2
        if playerOneTurn:
            choices[choice - 1] = 'X'
        else:
            choices[choice - 1] = 'O'

        # This is used for swapping between the 2 players
        playerOneTurn = not playerOneTurn

        # if-else statements to signify 3 in a row for horizontal, vertical or diagonal
        for x in range(0, 3):
            y = x * 3
            if choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]:
                winner = True
                printBoard()
            if choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]:
                winner = True
                printBoard()

        if ((choices[0] == choices[4] and choices[0] == choices[8]) or
                (choices[2] == choices[4] and choices[4] == choices[6])):
            winner = True
            printBoard()
        if winner:  # if there is a winner, use the "RoundWinner" variable to determine the player's name who won
            RoundWinner = str(int(playerOneTurn + 1))
            if RoundWinner:
                print(f"Congratulations! {player1}, You have won")
            else:
                print(f"Congratulations! {player2}, You have won")


# while True, run the game, after the game ends, if the reply is "y", keep running, if not, break
while True:
    tic_tac_toe()
    if input("Play again (y/n)\n") != "y":
        break
