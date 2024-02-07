from GameState import GameState, GameStateNode
from abc import ABC, abstractmethod
from Heuristics import Heuristics
from Queue import PriorityQueue, IQueue, IMetered, Queue

# Abstract class for search algorithms
class Search(ABC):
	@abstractmethod
	def solve(self, start: GameState):
		pass

# Breadth-first search algorithm
class BFS(Search):
	target: GameStateNode
	start: GameStateNode
	queue: IQueue[GameStateNode] | IMetered
	
	# Create a new breadth-first search algorithm with the given target game state
	def __init__(self, target: GameState, queue: IQueue[GameStateNode] = Queue()):
		self.target = GameStateNode(target)
		self.queue = queue
	
	# Solve the puzzle starting from the given game state
	def solve(self, start: GameState):
		self.start = GameStateNode(start)
		self.queue.put(self.start)
		while not self.queue.empty():
			node = self.queue.get()
			if node == self.target:
				return node.get_path()
			node.create_children()
			for child in node.children:
				if child == self.target:
					return child.get_path()
				if not node.is_in_path(child.game):
					self.queue.put(child)
		return None
	
	# Get the metrics of the search algorithm
	def get_metrics(self):
		if not isinstance(self.queue, IMetered):
			return None
		return self.queue.get_count(), len(self.queue), self.queue.get_count() - len(self.queue)


# A* search algorithm
class AStar(Search):
	target: GameState
	heuristics: Heuristics
	queue: IQueue[tuple[int, GameStateNode]] | IMetered
	
	# Create a new A* search algorithm with the given target game state, heuristics, and queue
	# The queue is a priority queue by default
	def __init__(self, target: GameState, heuristics: Heuristics, queue: IQueue[tuple[int, GameStateNode]] = PriorityQueue()):
		self.target = target
		self.heuristics = heuristics
		self.queue = queue
	
	# Solve the puzzle starting from the given game state
	def solve(self, start: GameState):
		start_node = GameStateNode(start)
		self.queue.put((0, start_node))
		while not self.queue.empty():
			_, node = self.queue.get()
			if node.game == self.target:
				return node.get_path()
			if node.is_in_path(self.target):
				continue
			node.create_children()
			for child in node.children:
				if not node.is_in_path(child.game):
					self.queue.put((self.heuristics(child.game) + child.depth, child))
		return None
	
	# Get the metrics of the search algorithm
	def get_metrics(self):
		if not isinstance(self.queue, IMetered):
			return None
		return self.queue.get_count(), len(self.queue), self.queue.get_count() - len(self.queue)
	
