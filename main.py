from GameState import GameState


class ManhattanDistance:
	target: GameState
	
	def __init__(self, target: GameState):
		self.target = target
	
	def calculate(self, game: GameState):
		distance = 0
		for i in range(len(game.board)):
			for j in range(len(game.board[i])):
				if game.board[i][j] != 0:
					distance += self.calculate_position(game.board[i][j], i, j)
		return distance
	
	def calculate_position(self, number, i, j):
		target_i, target_j = self.target.get_position(number)
		return abs(i - target_i) + abs(j - target_j)
	
	def __call__(self, game: GameState):
		return self.calculate(game)
		