
if __name__ == '__main__':
	hetman = hetman(4)

	open_queue = []
	heapq.heappush(open_queue, (0, []))

	while open_queue:
		priority, hetmans_array = heapq.heappop(open_queue)
		hetman.visited_counter = hetman.visited_counter + 1

		if len(hetmans_array) <= hetman.size:
			if hetman.check_correct(hetmans_array):
				hetman.solutions.extend([hetmans_array])

			children = hetman.generate_children(hetmans_array)

			for child in children:
				heuristics = hetman.heuristics_h1(child)
				heapq.heappush(open_queue, (heuristics, child))

	print(hetman.solutions)