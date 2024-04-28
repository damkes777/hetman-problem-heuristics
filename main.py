import heapq
import time
import hetman
import heuristics_h1
import heuristics_h2

if __name__ == '__main__':
	size = 8
	het = hetman.Hetman(size)
	# heuristics = heuristics_h2.HeuristicsH2(size)
	heuristics = heuristics_h1.HeuristicsH1(size)
	open_queue = []
	heapq.heappush(open_queue, (0, []))

	time_start = time.time()

	while open_queue:
		priority, hetmans_array = heapq.heappop(open_queue)

		if len(hetmans_array) <= het.size:
			het.visited_counter += 1
			if het.check_correct(hetmans_array):
				het.solutions.extend([hetmans_array])
				break

			if len(hetmans_array) != het.size:
				children = het.generate_children(hetmans_array)
				for child in children:
					hetman_heuristics = heuristics.calculate_heuristics(child)
					heapq.heappush(open_queue, (hetman_heuristics, child))

	time_end = time.time()
	final_time = round((time_end - time_start) * 1000, 2)

	print(final_time)
	print(het.solutions)
	print(het.generated_counter)
	print(het.visited_counter)

	with open('files/H1/generated.txt', 'a') as file:
		file.write("\n" + str(het.generated_counter))
		file.close()
	with open('files/H1/visited.txt', 'a') as file:
		file.write("\n" + str(het.visited_counter))
		file.close()
	with open('files/H1/times.txt', 'a') as file:
		file.write("\n" + str(final_time))
		file.close()

