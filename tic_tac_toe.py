from builtins import print


def display_board(game_board):
    print("\n")
    print('   |   |')
    print(' ' + game_board[0] + ' | ' + game_board[1] + ' | ' + game_board[2])
    print('---+---+---')
    print(' ' + game_board[3] + ' | ' + game_board[4] + ' | ' + game_board[5])
    print('   |   |')
    print('---+---+---')
    print(' ' + game_board[6] + ' | ' + game_board[7] + ' | ' + game_board[8])
    print('   |   |')


def player_input(player_name, game_board):
    choice = 0
    same = False
    while choice is not int and (choice < 1 or choice > 9) or same == False:
        choice = int(input(f"{player_name} choose b/w [1-9]: "))
        if game_board[choice-1] != '.':
            print("This place is already filled ! \n")
        else:
            same = True
    return choice


def player_marker():
    choice_list = ["X", "O"]
    input_choice = ""
    check = False
    while check == False:
        input_choice = input('Player 1 please choose [X or O] : ').upper()
        if input_choice in choice_list:
            check = True
        else:
            print("Invalid input. Only letters X and O are allowed")
    if input_choice == "X":
        print("Player 1 your marker is [X]")
        print("Player 2 your marker is [O] \n")
    else:
        print("Player 1 your marker is [O]")
        print("Player 2 your marker is [X] \n")
    return input_choice


def if_winner_player1(marker,game_board):
    player = ""
    if (   game_board[0] == game_board[1] == game_board[2] == marker or game_board[0] == game_board[3] == game_board[6] == marker
        or game_board[0] == game_board[4] == game_board[8] == marker or game_board[3] == game_board[4] == game_board[5] == marker
        or game_board[2] == game_board[4] == game_board[6] == marker or game_board[2] == game_board[5] == game_board[8] == marker
        or game_board[6] == game_board[7] == game_board[8] == marker or game_board[1] == game_board[4] == game_board[7] == marker):
            player = "yes"
    return player


def if_winner_player2(marker, game_board):
    player = ""
    if (   game_board[0] == game_board[1] == game_board[2] == marker or game_board[0] == game_board[3] == game_board[6] == marker
        or game_board[0] == game_board[4] == game_board[8] == marker or game_board[3] == game_board[4] == game_board[5] == marker
        or game_board[2] == game_board[4] == game_board[6] == marker or game_board[2] == game_board[5] == game_board[8] == marker
        or game_board[6] == game_board[7] == game_board[8] == marker or game_board[1] == game_board[4] == game_board[7] == marker):
            player = "yes"
    return player


def end_game():
    choice_list = ['Y', 'N']
    choice = ""
    while choice not in choice_list:
        choice = input("Do you want to continue [Y or N] ?  ").upper()
    if choice == 'Y':
        return False
    elif choice == "N":
        return True


def place_marker(index, marker, game_board):
    game_board[index] = marker


def board_full(game_board):
    check = True
    for items in range(0, 9):
        if game_board[items] == ".":
            return False
    return check


def main_menu():
    game_list = ['.', '.', '.', '.', '.', '.', '.', '.', '.']

    winner1_bool = False
    winner2_bool = False
    draw = False
    end_of_game = False
    display_board(game_list)
    print("\n")
    player1_marker = player_marker()

    if player1_marker == "X":
        player2_marker = "O"
    else:
        player2_marker = "X"

    for _ in range(0, 9):  # This will run for maximum 9 times as there are 9 places on the board

        display_board(game_list)  # Displays the game board initially & after both players' turn
        print("\n")

        player1_index = player_input("Player 1", game_list)          # Game logic for Player 1
        place_marker(player1_index - 1, player1_marker, game_list)

        winner_player1 = if_winner_player1(player1_marker, game_list)  # Checks if Player 1 has won
        if len(winner_player1) != 0:
            winner1_bool = True
            break

        draw = board_full(game_list)  # Checks if the game has been brought to a draw
        if draw:
            break

        display_board(game_list)  # Displays the updated board after player 1's turn
        print("\n")

        player2_index = player_input("Player 2", game_list)   # Game logic for Player 2
        place_marker(player2_index - 1, player2_marker, game_list)

        winner_player2 = if_winner_player2(player2_marker, game_list)  # Checks if Player 2 has won
        if len(winner_player2) != 0:
            winner2_bool = True
            break

        display_board(game_list)  # Displays the updated board after player 2's turn
        print("\n")

        end_of_game = end_game()  # Asks the player whether he wants to quit or not
        if end_of_game:
            break

    print("\n")
    display_board(game_list)
    print("\n")
    if winner1_bool:
        print("The winner of the match is Player 1")
    elif winner2_bool:
        print("The winner of the match is Player 2")
    elif draw:
        print("The match is a Draw !!")
    elif end_of_game:
        print("The match has been ended on Player's request !!")


# Calling main_menu() here

main_menu()
