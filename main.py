from GameState import GameState, MOVE_NAMES
from Heuristics import ManhattanDistance
from Search import AStar
from IQueue import MeteredPriorityQueue
from time import perf_counter_ns


# Main function
def main():
	# Create the target and start game states
	target = GameState().create(4)
	start = target.copy().shuffle(30)
	
	# Print the game states
	print("Target:")
	target.print()
	print("Start:")
	start.print()
	
	# Solve the puzzle
	manhattan = ManhattanDistance(target)
	ast = AStar(target, manhattan, MeteredPriorityQueue())
	start_time = perf_counter_ns()
	path = ast.solve(start)
	end_time = perf_counter_ns()
	
	# Print the solution
	if path is None:
		print("No solution")
	else:
		print(f"Solution: {len(path)} moves")
		print(f"Time: {(end_time - start_time)/1_000_000:6f} ms")
		# Print the metrics if available
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
	