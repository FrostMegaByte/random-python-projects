import numpy as np
import copy

# NOT EVEN CLOSE TO COMPLETE YET. ONLY THE HEAD OF THE SNAKE CAN MOVE AROUND THE BOARD CURRENTLY

START_LOCATION = [0, 0]

class Board:
  candyLocation = None
  oldSnakePosition = None

  def __init__(self, snake, width=10):
    self.width = width
    self.size = width * width
    self.board = np.chararray((width, width))
    self.board[:] = ''
    self.board[snake.position[0], snake.position[1]] = 's'
    self.snake = snake

  def updateSnakeLocation(self):
    self.board[self.snake.position[0], self.snake.position[1]] = 's'
    self.board[self.oldSnakePosition[0], self.oldSnakePosition[1]] = ''

class Snake:
  length = 3
  position = START_LOCATION

class Game:
  player = Snake()
  board = Board(player)
  game_over = False

  def main(self):
    while (self.game_over == False):
      print(self.board.board)
      direction = self.askUserInput()
      self.move(direction)
      self.checkBoundaryCrossing(self.player, self.board)
      self.board.updateSnakeLocation()

  def askUserInput(self):
    while (True):
      userInput = input("Where to go? Up, down, left or right? (u, d, l, r)\n")

      if (userInput in ["u", "d", "l", "r"]):
        break
      else:
        print("Incorrect input. Please try again.\n")
    return userInput

  def move(self, direction):
    self.board.oldSnakePosition = copy.deepcopy(self.player.position)

    if (direction == "u"):
      self.player.position[0] -= 1
    elif (direction == "d"):
      self.player.position[0] += 1
    elif (direction == "l"):
      self.player.position[1] -= 1
    else:
      self.player.position[1] += 1

  def checkBoundaryCrossing(self, snake, board):
    if (snake.position[0] < 0 or snake.position[1] < 0):
      self.gameOver()
    if (snake.position[0] > board.width or snake.position[1] > board.width):
      self.gameOver()

  def gameOver(self):
    self.game_over = True
    print("GAME OVER")

start = Game()
start.main()