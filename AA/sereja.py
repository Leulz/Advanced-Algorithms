entrada1 = [int(x) for x in raw_input().split()]
n = entrada1[0]
m = entrada1[1]

array = [int(x) for x in raw_input().split()]

cont = 1
s = set()
s.add(array[-1])
resp = [1 for i in range(n)]

for i in range(n-2,-1,-1):
    if array[i]!=array[i+1] and array[i] not in s:
        cont+=1        
        s.add(array[i])
    resp[i]=cont

for i in range(m):
	print resp[int(raw_input())-1]

