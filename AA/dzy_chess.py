nm = [int(x) for x in raw_input().split()]

n = nm[0]
m = nm[1]

board = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
	linha = list(raw_input())
	board[i] = linha

for i in range(n):
	for j in range(m):
		if board[i][j]=='-':
			continue
		if i%2==0:
			if j%2==0:
				board[i][j]='B'
			else:
				board[i][j]='W'
		else:
			if j%2==0:
				board[i][j]='W'
			else:
				board[i][j]='B'

for i in range(n):
	print ''.join(board[i])
		
