from GameState import GameState, MOVE_NAMES
from Heuristics import LinearConflict
from Search import AStar, BFS
from Queue import MeteredPriorityQueue, MeteredQueue
from time import perf_counter_ns



def run_astar(target, start):
	# Solve the puzzle
	manhattan = LinearConflict(target)
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

def run_bfs(target, start):
	# Solve the puzzle
	bfs = BFS(target, MeteredQueue())
	start_time = perf_counter_ns()
	path = bfs.solve(start)
	end_time = perf_counter_ns()
	
	# Print the solution
	if path is None:
		print("No solution")
	else:
		print(f"Solution: {len(path)} moves")
		print(f"Time: {(end_time - start_time)/1_000_000:6f} ms")
		# Print the metrics if available
		metrics = bfs.get_metrics()
		if metrics is not None:
			enqueued, in_queue, expanded = metrics
			print(f"Enqueued: {enqueued}, In queue: {in_queue}, Expanded: {expanded}")
		else:
			print("No metrics available")
		print(path)
		print([MOVE_NAMES[i] for i in path])

# Main function
def main():
	# Create the target and start game states
	target = GameState().create(4)
	start = GameState().fill([
		[15, 2,  1,  12],
		[8,  5,  6,  11],
		[4,  9,  10,  7],
		[3,  14,  13,  0],
	])
	# target = GameState().create(4)
	# start = GameState().create(4).shuffle(35)
	
	# Print the game states
	print("Target:")
	target.print()
	print("Start:")
	start.print()
	
	# Run the A* search algorithm
	print("A* search algorithm")
	run_astar(target.copy(), start.copy())
	
	print()
	
	# Run the breadth-first search algorithm
	# print("Breadth-first search algorithm")
	# run_bfs(target.copy(), start.copy())
		

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		pass
	# with cProfile.Profile() as pr:
	# 	try:
	# 		main()
	# 	except KeyboardInterrupt:
	# 		pass
	# 	pr.print_stats(sort="cumtime")
	# 	pr.dump_stats("main.prof")
	