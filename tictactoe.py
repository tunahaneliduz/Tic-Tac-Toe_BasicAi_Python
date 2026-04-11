import datetime
import random
import os

if not os.path.exists("files"):
    os.makedirs("files")

board = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
player_score = 0
computer_score = 0


def show_board():
    print("\t " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("\t-----------")
    print("\t " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("\t-----------")
    print("\t " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print()
    print("###############")
    print()


def player_won():
    for i in range(1, 11, 3):
        if board[i:i + 3] == ["X", "X", "X"]:
            print("Player won!")
            return True
    for i in range(1, 4):
        if board[i:(i + 7):3] == ["X", "X", "X"]:
            print("Player won!")
            return True
    if (board[1] == board[5] == board[9] == "X") or \
       (board[3] == board[5] == board[7] == "X"):
        print("Player won!")
        return True
    return False


def computer_won():
    for i in range(1, 11, 3):
        if board[i:i + 3] == ["O", "O", "O"]:
            print("Computer won!")
            return True
    for i in range(1, 4):
        if board[i:(i + 7):3] == ["O", "O", "O"]:
            print("Computer won!")
            return True
    if (board[1] == board[5] == board[9] == "O") or \
       (board[3] == board[5] == board[7] == "O"):
        print("Computer won!")
        return True
    return False


def block_player_win():

    if board[1:4].count("X") == 2:
        for i in range(1, 4):
            if board[i] == str(i):
                board[i] = "O"
                return True

    if board[4:7].count("X") == 2:
        for i in range(4, 7):
            if board[i] == str(i):
                board[i] = "O"
                return True

    if board[7:10].count("X") == 2:
        for i in range(7, 10):
            if board[i] == str(i):
                board[i] = "O"
                return True

    for line in [[1, 4, 7], [2, 5, 8], [3, 6, 9]]:
        if [board[i] for i in line].count("X") == 2:
            for i in line:
                if board[i] == str(i):
                    board[i] = "O"
                    return True

    if [board[1], board[5], board[9]].count("X") == 2:
        for i in [1, 5, 9]:
            if board[i] == str(i):
                board[i] = "O"
                return True

    if [board[3], board[5], board[7]].count("X") == 2:
        for i in [3, 5, 7]:
            if board[i] == str(i):
                board[i] = "O"
                return True

    return False


def player_move():
    while True:
        choice = input("Choose a number (1-9): ")
        if choice not in board or choice == "":
            print("Invalid move, try again.")
            continue
        index = int(choice)
        board[index] = "X"
        break


def moves_left():
    for i in range(1, len(board)):
        if board[i] == str(i):
            return True
    return False


def computer_move():
    if block_player_win():
        return
    while moves_left():
        index = random.randint(1, 9)
        if str(index) not in board:
            continue
        board[index] = "O"
        break


while True:
    show_board()
    player_move()

    if player_won():
        show_board()
        board = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        player_score += 1
        choice = input("Press X to exit, any key to continue: ")
        if choice.upper() == "X":
            break

    if not moves_left():
        print("No moves left! It's a draw.")
        board = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        continue

    computer_move()

    if computer_won():
        show_board()
        board = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        computer_score += 1
        choice = input("Press X to exit, any key to continue: ")
        if choice.upper() == "X":
            break


print(f"Final Score -> Player: {player_score} - Computer: {computer_score}")

with open("files/score.txt", "a") as f:
    f.write(f"{datetime.datetime.now()} > Player: {player_score} - Computer: {computer_score}\n")
