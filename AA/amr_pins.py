import math

MAX = 300000

r, x, y, xx, yy = map(int, raw_input().split())

dist_x = abs(x-xx)
dist_y = abs(y-yy)

dist = math.sqrt(dist_x**2 + dist_y**2)

for i in range(MAX):
	if (i*r) >= dist/2: #(i*(2*r)) >= dist
		print i
		break
