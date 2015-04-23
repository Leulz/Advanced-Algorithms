def satisfiable():
	colored = [-1]*(n)
	color = 1
	odd_components = 0
	
	for node in range(n):
		if colored[node] == -1:
			mark_component(node, color, colored)			
			for node_aux in range(n):
				if colored[node_aux]==color and parity[node_aux]==1:
					odd_components += 1
					break
			color+=1
	if odd_components > 1:
		return False
	else:
		return True
	

def mark_component(node, color, colored):
	colored[node] = color
	for neighbor in graph[node]:
		if colored[neighbor] != color:
			mark_component(neighbor, color, colored)

n, m = map(int, raw_input().split())

graph = [[] for i in range(n)]

for i in range(m):
	path = map(int, raw_input().split())
	graph[path[0] - 1].append(path[1] - 1)
	graph[path[1] - 1].append(path[0] - 1)

parity = map(int, raw_input().split())

def root():
	for i in range(n):
		if parity[i] == 1:
			return i
	return 0

def wrong_parity(node):
	return ((parity[node]%2==0 and new_parity[node]%2==1) or (parity[node]%2==1 and new_parity[node]%2==0))

def path(node, parent):
	visited[node] = True
	new_parity[node] += 1
	ans_path.append(node + 1)
	
	for neighbor in graph[node]:
		if not visited[neighbor]:
			path(neighbor, node)
			ans_path.append(node + 1)
			new_parity[node] += 1
	
	if wrong_parity(node) and parent != -1:
		ans_path.append(parent + 1)
		new_parity[parent] += 1
		ans_path.append(node + 1)
		new_parity[node] += 1 

if satisfiable():
	visited = [False] * n
	new_parity = [0] * n
	
	ans_path = []
	
	root = root()
	
	path(root, -1)
	
	if wrong_parity(root):
		ans_path.pop()
	
	print len(ans_path)
	if len(ans_path)>0:
		print ' '.join(map(str,ans_path))
else:
	print -1
