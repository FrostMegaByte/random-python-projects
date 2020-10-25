import numpy as np

sudoku = [[0,0,0,2,6,0,7,0,1],
          [6,8,0,0,7,0,0,9,0],
          [1,9,0,0,0,4,5,0,0],
          [8,2,0,1,0,0,0,4,0],
          [0,0,4,6,0,2,9,0,0],
          [0,5,0,0,0,3,0,2,8],
          [0,0,9,3,0,0,0,7,4],
          [0,4,0,0,5,0,0,3,6],
          [7,0,3,0,1,8,0,0,0]]

def possible(column, row, value_to_check):
  global sudoku

  # Check if row contains `value_to_check`.
  for i in range(9):
    if sudoku[column][i] == value_to_check:
      return False
  
  # Check if column contains `value_to_check`.
  for i in range(9):
    if sudoku[i][row] == value_to_check:
      return False

  # Check if square contains `value_to_check`.
  row0 = (row//3)*3
  column0 = (column//3)*3
  for i in range(3):
    for j in range(3):
      if sudoku[column0+i][row0+j] == value_to_check:
        return False
  
  # Ultimately, if the move is possible. Return true.
  return True

def solve():
  global sudoku

  # Check every column and row.
  for column in range(9):
    for row in range(9):
      # If there is an empty value, check which value is possible and set it.
      if sudoku[column][row] == 0:
        for new_value in range(1, 10):
          if possible(column, row, new_value):
            sudoku[column][row] = new_value
            # Use recursion to backtrack by setting values back to an emtpy value if it took a 'wrong route'.
            solve()
            sudoku[column][row] = 0
        return
  print(np.matrix(sudoku))
  input('More solutions?')

solve()