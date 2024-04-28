class HeuristicsH2:
	def __init__(self, size):
		self.size = size

	def calculate_heuristics(self, hetmans):
		row_beating = self.beating_in_row(hetmans)
		diagonal_beating = self.beating_in_diagonal(hetmans)

		heuristics = (row_beating + diagonal_beating) + (self.size - len(hetmans))

		return heuristics

	@staticmethod
	def beating_in_row(hetmans):
		beating = (abs(len(hetmans) - len(set(hetmans)))) * 2

		return beating

	@staticmethod
	def beating_in_diagonal(hetmans):
		beating = 0

		for i in range(len(hetmans)):
			for j in range(i + 1, len(hetmans)):
				if abs(hetmans[i] - hetmans[j]) == abs(i - j):
					beating += 1

		return beating
