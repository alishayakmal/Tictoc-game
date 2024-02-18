def initialize_board():
    """Creates a 3x3 game board"""
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    """Prints the game board"""
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def player_input(board, player):
    """Allows players to enter their moves"""
    while True:
        try:
            row = int(input(f"Player {player}, enter your move row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter your move column (1-3): ")) - 1
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("This cell is already taken. Please choose another cell.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 1 and 3.")

def check_win(board, player):
    """Checks for a win"""
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def check_tie(board):
    """Checks for a tie"""
    for row in board:
        if ' ' in row:
            return False
    return True

def switch_player(player):
    """Switches the player"""
    return 'O' if player == 'X' else 'X'

def main():
    """Main game loop"""
    board = initialize_board()
    current_player = 'X'
    while True:
        print_board(board)
        player_input(board, current_player)
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        current_player = switch_player(current_player)
    if input("Play again? (y/n): ").lower() == 'y':
        main()

if __name__ == "__main__":
    main()