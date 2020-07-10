from Stack import Stack

adj_list = {
	"A":["B", "D"],
	"B":["A", "C"],
	"C":["B"],
	"D":["A", "E", "F"],
	"E":["D", "F", "G"],
	"F":["D", "E", "H"],
	"G":["E", "H"],
	"H":["G", "F"]
}


visited = {}
level = {}
parent = {}
dfs_traverse_nodes = []
stack = Stack()

for node in adj_list.keys():
	visited[node] = False
	level[node] = -1
	parent[node] = None

source = "A"
visited[source] = True
level[source] = 0
stack.push(source)

while not stack.is_empty():
	u = stack.pop()
	dfs_traverse_nodes.append(u)

	for v in adj_list[u]:
		if not visited[v]:
			visited[v] = True
			parent[v] = u
			level[v] = level[u] + 1
			stack.push(v)


print(dfs_traverse_nodes)
