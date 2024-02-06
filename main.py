from GameState import GameState, GameStateNode
from Search import Search
from queue import PriorityQueue


class ManhattanDistance:
	target: GameState
	positions: list[tuple[int, int]]
	
	def __init__(self, target: GameState):
		self.target = target
		self.positions = [(0, 0) for _ in range(target.size ** 2)]
		for i in range(target.board.shape[0]):
			for j in range(target.board.shape[1]):
				self.positions[target.board[i][j]] = (i, j)
	
	def calculate(self, game: GameState):
		distance = 0
		for i in range(game.board.shape[0]):
			for j in range(game.board.shape[1]):
				if game.board[i][j] != 0:
					x, y = self.positions[game.board[i][j]]
					distance += abs(x - i) + abs(y - j)
		return distance
	
	def __call__(self, game: GameState):
		return self.calculate(game)


class AStar(Search):
	target: GameState
	heuristics: ManhattanDistance
	queue: PriorityQueue[(int, GameStateNode)]
	
	def __init__(self, target: GameState, heuristics: ManhattanDistance):
		self.target = target
		self.heuristics = heuristics
		
	def solve(self, start: GameState):
		self.queue = PriorityQueue()
		start_node = GameStateNode(start)
		self.queue.put((0, start_node))
		while not self.queue.empty():
			temp = self.queue.get()
			node: GameStateNode = temp[1]
			if node.game == self.target:
				return node.get_path()
			if node.is_in_path(self.target):
				continue
			node.create_children()
			for child in node.children:
				if not node.is_in_path(child.game):
					self.queue.put((self.heuristics(child.game), child))
		return None
	
	