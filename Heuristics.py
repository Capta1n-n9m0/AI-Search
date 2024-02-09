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
	def distance(self, game: GameState):
		distance = 0
		for i in range(game.board.shape[0]):
			for j in range(game.board.shape[1]):
				x, y = self.positions[game.board[i][j]]
				distance += abs(x - i) + abs(y - j)
		return distance
	
	def __call__(self, game: GameState):
		return self.distance(game)
	
	
class LinearConflict(Heuristics):
	target: GameState
	# List of positions of the numbers in the target game state
	positions: list[tuple[int, int]]
	
	# Create a new Linear Conflict heuristics for the given target game state
	def __init__(self, target: GameState):
		self.target = target
		self.positions = [(0, 0) for _ in range(target.size ** 2)]
		for i in range(target.board.shape[0]):
			for j in range(target.board.shape[1]):
				self.positions[target.board[i][j]] = (i, j)
		
	# Calculate the Manhattan distance for the given game state
	def distance(self, game: GameState):
		distance = 0
		for i in range(game.board.shape[0]):
			for j in range(game.board.shape[1]):
				x, y = self.positions[game.board[i][j]]
				distance += abs(x - i) + abs(y - j)
		return distance

	def horizontal_conflict(self, game: GameState):
		conflicts = 0
		for row in range(game.size):
			for i in range(game.size):
				for j in range(i, game.size):
					pa = self.positions[game.board[row, i]]
					pb = self.positions[game.board[row, j]]
					if pa[1] < pb[1]:
						conflicts += 1
		return conflicts
	
	def vertical_conflict(self, game: GameState):
		conflicts = 0
		for col in range(game.size):
			for i in range(game.size):
				for j in range(i, game.size):
					pa = self.positions[game.board[i, col]]
					pb = self.positions[game.board[j, col]]
					if pa[0] < pb[0]:
						conflicts += 1
		return conflicts
	
	def __call__(self, game: GameState):
		return self.distance(game) + (self.horizontal_conflict(game) + self.vertical_conflict(game)) * 2
	