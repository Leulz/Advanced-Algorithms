nmk = [int(x) for x in raw_input().split()]

n = nmk[0]
m = nmk[1]
k = nmk[2]

graph = [[0 for x in range(m)] for y in range(n)]
used = [[False for x in range(m)] for y in range(n)]
validos = []


for i in range(n):
	entrada = list(raw_input())
	for j in range(len(entrada)):
		graph[i][j] = entrada[j]
		if entrada[j] == '.':
			validos.append((i,j))

k = len(validos) - k

def is_valid_position(x,y):
	if x>=0 and x<n and y>=0 and y<m:
		return True
	return False

pos_x = [1,-1,0,0]
pos_y = [0,0,1,-1]

def dfs(x, y):
	used[x][y] = True
	global k
	k-=1
	
	for i in range(4):
		if k!=0:
			u = x+pos_x[i]
			v = y+pos_y[i]
			if is_valid_position(u,v):
				if graph[u][v] == '.':
					if not used[u][v]:
						dfs(u,v)

dfs(validos[0][0],validos[0][1])

for i in range(len(validos)):
	if not used[validos[i][0]][validos[i][1]]:
		graph[validos[i][0]][validos[i][1]] = 'X'

for i in range(n):
	print ''.join(graph[i])

