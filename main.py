from GameState import GameState, MOVE_NAMES
from Heuristics import ManhattanDistance
from Search import AStar
from IQueue import MeteredPriorityQueue


def main():
	target = GameState().create(4)
	start = target.copy().shuffle(30)
	
	print("Target:")
	target.print()
	print("Start:")
	start.print()
	
	manhattan = ManhattanDistance(target)
	ast = AStar(target, manhattan, MeteredPriorityQueue())
	path = ast.solve(start)
	if path is None:
		print("No solution")
	else:
		print(f"Solution: {len(path)} moves")
		metrics = ast.get_metrics()
		if metrics is not None:
			enqueued, in_queue, expanded = metrics
			print(f"Enqueued: {enqueued}, In queue: {in_queue}, Expanded: {expanded}")
		else:
			print("No metrics available")
		print(path)
		print([MOVE_NAMES[i] for i in path])
		

if __name__ == "__main__":
	main()
	