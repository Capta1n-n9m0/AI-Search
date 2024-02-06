from GameState import GameState, MOVE_NAMES
from Heuristics import ManhattanDistance
from Search import AStar


def main():
	target = GameState().create(5)
	start = GameState().create(5).shuffle(50)
	
	print("Target:")
	target.print()
	print("Start:")
	start.print()
	
	manhattan = ManhattanDistance(target)
	ast = AStar(target, manhattan)
	path = ast.solve(start)
	if path is None:
		print("No solution")
	else:
		print(f"Solution: {len(path)} moves")
		print(path)
		print([MOVE_NAMES[i] for i in path])
		

if __name__ == "__main__":
	main()
	