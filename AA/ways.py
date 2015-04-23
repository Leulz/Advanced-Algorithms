n = int(raw_input())
array = [int(x) for x in raw_input().split()]
soma1 = sum(array)

if soma1%3!=0 or len(array)<=2:
	print 0
else:
	ocorrencias = [0 for x in range(n)]
	s = 0
	div = soma1/3
	
	for i in range(n-1,-1,-1):
		s+=array[i]
		if s==div:
			ocorrencias[i]=1
	for i in range(n-2, -1, -1):
		ocorrencias[i]+=ocorrencias[i+1]
	resp = 0
	s = 0
	for i in range(n-2):
		s+=array[i]
		if s==div:
			resp+=ocorrencias[i+2]
	print resp
