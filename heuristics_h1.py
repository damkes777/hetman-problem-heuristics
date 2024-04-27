class HeuristicsH1:
	def __init__(self, size):
		self.size = size

	def calculate_heuristics(self, hetmans):
		hetmans_weight = []

		for hetman in hetmans:
			if hetman <= self.size / 2:
				weight = self.size - hetman + 1
				hetmans_weight.append(weight)
			else:
				hetmans_weight.append(hetman)

		heuristics = (self.size - len(hetmans)) * sum(hetmans_weight)

		return heuristics
