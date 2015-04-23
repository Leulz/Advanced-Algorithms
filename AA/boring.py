n = int(raw_input())

entrada = [int(x) for x in raw_input().split()]

array = [0 for x in range(100012)]
maximo = max(entrada)

for i in entrada:
	array[i]+=1

pd = [0 for x in range(100012)]
pd[1]=array[1]

for i in range(2,maximo+1):
	pd[i]=max(pd[i-1],pd[i-2]+array[i]*i)

print pd[maximo]
