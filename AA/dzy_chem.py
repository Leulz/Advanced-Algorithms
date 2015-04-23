import math


nm = [int(x) for x in raw_input().split()]
n = nm[0]
m = nm[1]

graph = {}

def make_link(G,x,y):
	if x not in G:
		G[x] = []
	(G[x]).append(y)
	if y not in G:
		G[y] = []
	(G[y]).append(x)
	return G
for i in range(m):
	substances = [int(x) for x in raw_input().split()]
	make_link(graph,substances[0],substances[1])

def mark_component(G, node, marked):
	marked[node] = True
	total_marked = 1
	for neighbor in G[node]:
		if neighbor not in marked:
			total_marked += mark_component(G, neighbor, marked)
	return total_marked
mark = {}
components = 0
for i in graph.keys():
	if i not in mark:
		components+=1
	mark_component(graph, i, mark)

print int(math.pow(2, len(graph)-components))
