board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def display():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])


def winner():
    if board[0] == board[1] == board[2] and board[0] != " ":
        return board[0]

    if board[3] == board[4] == board[5] and board[3] != " ":
        return board[3]

    if board[6] == board[7] == board[8] and board[6] != " ":
        return board[6]

    if board[0] == board[3] == board[6] and board[0] != " ":
        return board[0]

    if board[1] == board[4] == board[7] and board[1] != " ":
        return board[1]

    if board[2] == board[5] == board[8] and board[2] != " ":
        return board[2]

    if board[0] == board[4] == board[8] and board[0] != " ":
        return board[0]

    if board[2] == board[4] == board[6] and board[2] != " ":
        return board[2]

    return " "


print("TIC TAC TOE")
print("YOU = X")
print("AI = O")

while True:

    display()

    # Human move
    position = int(input("Enter position (1-9): "))

    if position >= 1 and position <= 9:

        position = position - 1

        if board[position] == " ":
            board[position] = "X"
        else:
            print("Position already taken")
            continue

    else:
        print("Enter number between 1 and 9")
        continue

    # Check human winner
    if winner() == "X":
        display()
        print("YOU WIN!")
        break

    # AI move
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            break

    print("AI MOVE")
    display()

    # Check AI winner
    if winner() == "O":
        print("AI WINS!")
        break

    # Check draw
    if " " not in board:
        print("DRAW!")
        break