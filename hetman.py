class Hetman:
	def __init__(self, size):
		self.size = size
		self.visited_counter = 0
		self.generated_counter = 0
		self.solutions = []

	def generate_children(self, parent):
		children = []
		for i in range(1, self.size + 1):
			self.generated_counter += 1

			parent_template = parent.copy()
			parent_template.append(i)
			children.extend([parent_template])

		return children

	def check_correct(self, to_check):
		if not self.check_hetman(to_check):
			return False

		if not self.check_row(to_check):
			return False

		if not self.check_diagonal(to_check):
			return False

		return True

	def check_hetman(self, to_check):
		return len(to_check) == self.size

	@staticmethod
	def check_row(to_check):
		return len(to_check) == len(set(to_check))

	@staticmethod
	def check_diagonal(to_check):
		for i in range(len(to_check)):
			for j in range(i + 1, len(to_check)):
				if abs(to_check[i] - to_check[j]) == abs(i - j):
					return False

		return True
