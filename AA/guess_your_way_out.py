import math

h, n = map(int, raw_input().split())

level = math.pow(2, h)

current_node = n

current_node_parity = n % 2

left_or_right = 0 # -1 if left of tree, 1 if right

if current_node>level/2:
	left_or_right = 1
else:
	left_or_right = -1

ans = current_node - 1


while level!=1:	
	current_node = math.ceil(current_node/2.0)	
	
	ans += current_node
	
	level /= 2
	
	
	print level
	print current_node
	print ans
	
	
	
	
print int(ans)
