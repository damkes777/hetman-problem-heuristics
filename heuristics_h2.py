class HeuristicsH2:
	def __init__(self, hetmans, size):
		self.hetmans = hetmans
		self.size = size

	def calculate_heuristics(self):
		row_beating = self.beating_in_row()
		diagonal_beating = self.beating_in_diagonal()

		heuristics = (row_beating + diagonal_beating) + (self.size - len(self.hetmans))

		return heuristics

	def beating_in_row(self):
		beating = (abs(len(self.hetmans) - len(set(self.hetmans)))) * 2

		return beating

	def beating_in_diagonal(self):
		beating = 0

		for i in range(len(self.hetmans)):
			for j in range(i + 1, len(self.hetmans)):
				if abs(self.hetmans[i] - self.hetmans[j]) == abs(i - j):
					beating += 1

		return beating
