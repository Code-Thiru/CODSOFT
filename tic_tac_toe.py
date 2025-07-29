import math
board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print(" | ".join(row))
        if i < 2:
            print("---------")
    print()

def is_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   
        [0, 4, 8], [2, 4, 6]               
    ]
    return any(all(board[i] == player for i in combo) for combo in win_conditions)

def is_board_full():
    return " " not in board

def minimax(depth, is_maximizing):
    if is_winner("O"):
        return 1
    elif is_winner("X"):
        return -1
    elif is_board_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

def human_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == " ":
            board[int(move) - 1] = "X"
            break
        else:
            print("Invalid move. Try again.")

def play_game():
    print("TIC-TAC-TOE: You (X) vs AI (O)")
    print_board()

    while True:
        human_move()
        print_board()
        if is_winner("X"):
            print("You win!")
            break
        if is_board_full():
            print("It's a draw!")
            break

        ai_move()
        print("AI's move:")
        print_board()
        if is_winner("O"):
            print("AI wins!")
            break
        if is_board_full():
            print("It's a draw!")
            break

play_game()
