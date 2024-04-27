import heapq
import time
import hetman
import heuristics_h1

if __name__ == '__main__':
	het = hetman.Hetman(4)
	heuristics = heuristics_h1.HeuristicsH1(4)
	open_queue = []
	heapq.heappush(open_queue, (0, []))

	time_start = time.time()
	while open_queue:
		priority, hetmans_array = heapq.heappop(open_queue)

		if len(hetmans_array) <= het.size:
			het.visited_counter += 1
			if het.check_correct(hetmans_array):
				het.solutions.extend([hetmans_array])

			if len(hetmans_array) != het.size:
				children = het.generate_children(hetmans_array)
				for child in children:
					hetman_heuristics = heuristics.calculate_heuristics(child)
					heapq.heappush(open_queue, (hetman_heuristics, child))
	time_end = time.time()
	final_time = (time_end - time_start) * 1000

	print(final_time)
	print(het.solutions)
	print(het.generated_counter)
	print(het.visited_counter)
