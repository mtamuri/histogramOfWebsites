def main():
  # Create a new Tic-Tac-Toe board
  board = [[None, None, None],
           [None, None, None],
           [None, None, None]]

  # Initialize the current player
  current_player = 'X'

  # Play the game until it is over
  while True:
    # Print the current board
    print_board(board)

    # Get the move for the current player
    move = get_move(current_player)

    # Make the move on the board
    board[move[0]][move[1]] = current_player

    # Check if the game is over
    if is_game_over(board):
      break

    # Switch players
    current_player = 'O' if current_player == 'X' else 'X'

  # Print the final board
  print_board(board)

  # Determine the winner
  winner = get_winner(board)

  # Print the winner
  if winner is not None:
    print(f'{winner} wins!')
  else:
    print('Tie!')


def print_board(board):
  for row in board:
    print(' '.join(row))


def get_move(player):
  while True:
    move = input(f'{player}, enter your move (row, col): ')

    try:
      row, col = move.split(',')
      row = int(row)
      col = int(col)

      if 0 <= row < 3 and 0 <= col < 3:
        if board[row][col] is None:
          return (row, col)
        else:
          print('That space is already taken.')
      else:
        print('Invalid move.')
    except ValueError:
      print('Invalid move.')


def is_game_over(board):
  # Check if there is a winner
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
      return True

  for i in range(3):
    if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
      return True

  if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
    return True

  if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
    return True

  # Check if the board is full
  for row in board:
    for cell in row:
      if cell is None:
        return False

  # If there is no winner and the board is full, then the game is a tie
  return True


def get_winner(board):
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
      return board[i][0]

  for i in range(3):
    if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
      return board[0][i]

  if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
    return board[0][0]

  if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
    return board[0][2]

  return None


if __name__ == '__main__':
  main()
