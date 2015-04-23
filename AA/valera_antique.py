n, v = map(int, raw_input().split())

seller_num = 1
satisfied_sellers = 0
ans = []
for i in range(n):
	seller = map(int, raw_input().split())
	
	for j in range(1, len(seller)):
		if seller[j] < v:
			ans.append(seller_num)
			satisfied_sellers += 1
			break
	seller_num += 1

print satisfied_sellers
if len(ans)>0:
	print ' '.join(map(str, ans))
