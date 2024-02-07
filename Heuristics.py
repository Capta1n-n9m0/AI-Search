from abc import abstractmethod, ABC
from GameState import GameState


# Abstract class for heuristics
class Heuristics(ABC):
	@abstractmethod
	def __call__(self, game: GameState):
		pass


# Heuristics implementation using the Manhattan distance
class ManhattanDistance(Heuristics):
	target: GameState
	# List of positions of the numbers in the target game state
	positions: list[tuple[int, int]]
	
	# Create a new Manhattan distance heuristics for the given target game state
	def __init__(self, target: GameState):
		self.target = target
		self.positions = [(0, 0) for _ in range(target.size ** 2)]
		for i in range(target.board.shape[0]):
			for j in range(target.board.shape[1]):
				self.positions[target.board[i][j]] = (i, j)
	
	# Calculate the Manhattan distance for the given game state
	def calculate(self, game: GameState):
		distance = 0
		for i in range(game.board.shape[0]):
			for j in range(game.board.shape[1]):
				x, y = self.positions[game.board[i][j]]
				distance += abs(x - i) + abs(y - j)
		return distance
	
	def __call__(self, game: GameState):
		return self.calculate(game)
	