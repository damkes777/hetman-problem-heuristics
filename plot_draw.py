import matplotlib.pyplot as plt

data_h1 = []
with open('files/H1/visited.txt', 'r') as file:
	for line in file:
		data_h1.append(int(line.strip()))

data_h2 = []
with open('files/H2/visited.txt', 'r') as file:
	for line in file:
		data_h2.append(int(line.strip()))

n_range = range(4, 9)
plt.plot(n_range, data_h1, marker='o', label='H1')
plt.plot(n_range, data_h2, marker='o', label='H2')
plt.title('Heurystyka H2 vs H1, odwiedzenia do pierwszego rozwiązania')
plt.xlabel('Wielkość N')
plt.ylabel('Odwiedzenia')
plt.grid(True)
plt.legend()
plt.savefig('plots/compare/visited.png')
plt.show()
