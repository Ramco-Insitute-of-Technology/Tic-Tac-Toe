import random
board = [" " for i in range(9)]
def print_board():
  for i in range(0,9,3):
    print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
    if i <6:
      print("-"*9)
def win(board, player):
  combination = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8},
                {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
                {0, 4, 8}, {2, 4, 6}]
  for a, b, c in combination:
    if board[a] == board[b] == board[c] == player:
      return True
  return False
def play_game():
  print('welcome to Tic-Tac-Toe')
  print_board()
  while True:
    move = int(input('Enter your move(1-9): ')) -1
    if board[move] == " ":
      board[move] = "X"
    else:
      print("Invalid move. Try again")
      continue
    print_board()
    if win(board, "X"):
      print("You win!")
      break
    if " " not in board:
      print("It is a tie")
      break
    move = random.choice([i for i, spot in enumerate(board) if spot == " "])
    board[move] = '0'
    print(f"AI Plays{move+1}:")
    print_board()
    if win(board, '0'):
      print("AI wins")
      break
play_game()
