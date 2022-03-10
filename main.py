
game = input("Do you want to play with a CPU or with another player? (answer with CPU or 2player):\n")

game = game.lower()

if game == "2player":
  board1 = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
  ]
  
  board2 = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
  ]
  
  #Instead of "-" placeholders we use " " placeholders to make it   more efficient
  
  letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
  }
  
  #We use letters on the x axis to stay original to the battleship   game
  
  def ask_user_for_board_position():
    column = input("column (A to H):")
    column = column.upper()
  
    while column not in "ABCDEFGH":
      print("That column is wrong! It should be A, B, C, D, E, F,    G, or H")
      column = input("column (A to H):")
      column = column.upper()
  
    row = input("row (1 to 8):")
  
    while row not in "12345678":
      print("That row is wrong! it should be 1, 2, 3, 4, 5, 6, 7,    8")
      row = input("row (1 to 8):")
    
    
    return int(row) - 1, letters_to_numbers[column]
  
  def print_board(board):
    print("  A B C D E F G H")
    print(" +-+-+-+-+-+-+-+-+") 
    row_number = 1
    for row in board:
      print("%d|%s|" % (row_number, "|".join(row)))
      print(" +-+-+-+-+-+-+-+-+")
      row_number = row_number + 1
  
  # This is to create a board that clearly shows the values where you can guess
  
  for n in range(5):
    print("Player 1, Where do you want ship", n + 1, "?")
    row_number, column_number = ask_user_for_board_position()
  
    if board1[row_number][column_number] == '*':
      print("That spot already has a battleship in it!")
  
    board1[row_number][column_number] = '*'
    print_board(board1)
  
  print("\n"*50)
  
  #This is asking for player 1's ships
  
  for n in range(5):
    print("Player 2, Where do you want ship ", n + 1, "?")
    row_number, column_number = ask_user_for_board_position()
  
    if board2[row_number][column_number] == '*':
      print("That spot already has a battleship in it!")
  
    board2[row_number][column_number] = '*'
    print_board(board2)
  
  #This is asking for player 2's ships
  
  
  print("\n"*50)
  #This is so you cant see where ships were placed, but can look     back for debugging
  
  guesses_board1 = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
  ]
  
  guesses_board2 = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
  ]
  
  #This is so there can be 2 boards for each player, and then we     can compare if there are values in those boards to the player's    boards, and as well as seeing if there is anything there, we can   check what is there
  
  
  guesses1 = 0
  counter1 = 0
  while guesses1 < 10:
    print("Player 2, Guess a battleship location")
    row_number, column_number = ask_user_for_board_position()
  
    if guesses_board1[row_number][column_number] != ' ':
      print("You have already guessed that place!")
      continue
    if board1[row_number][column_number] == '*':
      print("HIT!")
      guesses_board1[row_number][column_number] = '!'
      guesses1 += 2
      counter1 += 1
    else:
      guesses_board1[row_number][column_number] = 'X'
      print("MISS!")
      guesses1 += 1
  
    print_board(guesses_board1)
  
  print("You took down", counter1, "ships!")
  
  
  guesses2 = 0
  counter2 = 0
  while guesses2 < 10:
    print("Player 1, Guess a battleship location")
    row_number, column_number = ask_user_for_board_position()
  
    if guesses_board2[row_number][column_number] != ' ':
      print("You have already guessed that place!")
      continue
    
    if board2[row_number][column_number] == '*':
      print("HIT!")
      guesses_board2[row_number][column_number] = '!'
      guesses2 += 2
      counter2 += 1
    else:
      guesses_board2[row_number][column_number] = 'X'
      print("MISS!")
      guesses2 += 1
      
  
    print_board(guesses_board2)
  
  print("You took down", counter2, "ships!")
  
  if counter2 > counter1 :
    print("Player 1 wins!")
  elif counter1 > counter2 :
    print("Player 2 wins!")
  else:
    print("Its a Draw!"*5)
  
  print("GAME OVER!")

elif game == "cpu":
  from random import randint
  import os
  
  #Ship Class
  class Ship:
    def __init__(self, size, orientation, location):
      self.size = size
  
      if orientation == 'horizontal' or orientation == 'vertical':
        self.orientation = orientation
      else:
        raise ValueError("Value must be 'horizontal' or     'vertical'.")
  
      if orientation == 'horizontal':
        if location['row'] in range(row_size):
          self.coordinates = []
          for index in range(size):
            if location['col'] + index in range(col_size):
              self.coordinates.append({'row': location['row'],   'col': location['col'] + index})
            else:
              raise IndexError("Column is out of range.")
        else:
          raise IndexError("Row is out of range.")
      elif orientation == 'vertical':
        if location['col'] in range(col_size):
          self.coordinates = []
          for index in range(size):
            if location['row'] + index in range(row_size):
              self.coordinates.append({'row': location['row'] + index, 'col': location['col']})
            else:
              raise IndexError("Row is out of range.")
        else:
          raise IndexError("Column is out of range.")
  
      if self.filled():
        print_board(board)
        print(" ".join(str(coords) for coords in self.coordinates))
        raise IndexError("A ship already occupies that space.")
      else:
        self.fillBoard()
  
    def filled(self):
      for coords in self.coordinates:
        if board[coords['row']][coords['col']] == 1:
          return True
      return False
  
    def fillBoard(self):
      for coords in self.coordinates:
        board[coords['row']][coords['col']] = 1
  
    def contains(self, location):
      for coords in self.coordinates:
        if coords == location:
          return True
      return False
  
    def destroyed(self):
      for coords in self.coordinates:
        if board_display[coords['row']][coords['col']] == 'O':
          return False
        elif board_display[coords['row']][coords['col']] == '*':
          raise RuntimeError("Board display inaccurate")
      return True
  
  
  #Settings Variables
  row_size = 9 #number of rows
  col_size = 9 #number of columns
  num_ships = 4
  max_ship_size = 5
  min_ship_size = 2
  num_turns = 40
  
  #Create lists
  ship_list = []
  
  board = [[0] * col_size for x in range(row_size)]
  
  board_display = [["O"] * col_size for x in range(row_size)]
  
  #Functions
  def print_board(board_array):
    print("\n  " + " ".join(str(x) for x in range(1, col_size + 1)))
    for r in range(row_size):
      print(str(r + 1) + " " + " ".join(str(c) for c in board_array[r]))
    print()
  
  def search_locations(size, orientation):
    locations = []
  
    if orientation != 'horizontal' and orientation != 'vertical':
      raise ValueError("Orientation must have a value of either 'horizontal' or 'vertical'.")
  
    if orientation == 'horizontal':
      if size <= col_size:
        for r in range(row_size):
          for c in range(col_size - size + 1):
            if 1 not in board[r][c:c+size]:
              locations.append({'row': r, 'col': c})
    elif orientation == 'vertical':
      if size <= row_size:
        for c in range(col_size):
          for r in range(row_size - size + 1):
            if 1 not in [board[i][c] for i in range(r, r+size)]:
              locations.append({'row': r, 'col': c})
  
    if not locations:
      return 'None'
    else:
      return locations
  
  def random_location():
    size = randint(min_ship_size, max_ship_size)
    orientation = 'horizontal' if randint(0, 1) == 0 else 'vertical'
  
    locations = search_locations(size, orientation)
    if locations == 'None':
      return 'None'
    else:
      return {'location': locations[randint(0, len(locations) - 1)], 'size': size,\
       'orientation': orientation}
  
  def get_row():
    while True:
      try:
        guess = int(input("Row Guess: "))
        if guess in range(1, row_size + 1):
          return guess - 1
        else:
          print("\nOops, that's not even in the ocean.")
      except ValueError:
        print("\nPlease enter a number")
  
  def get_col():
    while True:
      try:
        guess = int(input("Column Guess: "))
        if guess in range(1, col_size + 1):
          return guess - 1
        else:
          print("\nOops, that's not even in the ocean.")
      except ValueError:
        print("\nPlease enter a number")
  
  # Create the ships
  
  temp = 0
  while temp < num_ships:
    ship_info = random_location()
    if ship_info == 'None':
      continue
    else:
      ship_list.append(Ship(ship_info['size'], ship_info['orientation'], ship_info['location']))
      temp += 1
  del temp
  
  # Play Game
  os.system('clear')
  print_board(board_display)
  
  for turn in range(num_turns):
    print("Turn:", turn + 1, "of", num_turns)
    print("Ships left:", len(ship_list))
    print()
  
    guess_coords = {}
    while True:
      guess_coords['row'] = get_row()
      guess_coords['col'] = get_col()
      if board_display[guess_coords['row']][guess_coords['col']] == 'X' or \
       board_display[guess_coords['row']][guess_coords['col']] == '*':
        print("\nYou guessed that one already.")
      else:
        break
  
    os.system('clear')
  
    ship_hit = False
    for ship in ship_list:
      if ship.contains(guess_coords):
        print("Hit!")
        ship_hit = True
        board_display[guess_coords['row']][guess_coords['col']] = 'X'
        if ship.destroyed():
          print("Ship Destroyed!")
          ship_list.remove(ship)
        break
    if not ship_hit:
      board_display[guess_coords['row']][guess_coords['col']] = '*'
      print("You missed!")
  
    print_board(board_display)
  
    if not ship_list:
      break
  
  # End Game
  if ship_list:
    print("You lose!")
  else:
    print("All the ships are sunk. You win!")
else:
  print("Error!")