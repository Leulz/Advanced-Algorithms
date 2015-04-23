n = int(raw_input())

for case in range(n):
	values = map(int, raw_input().split())
	
	a = (values[0],values[1])
	b = (values[2],values[3])
	c = (values[4],values[5])
	d = (values[6],values[7])
	r = (values[8],values[9])
	
	menorx = a[0]
	
	if menorx>b[0]:
		menorx = b[0]
	if menorx>c[0]:
		menorx = c[0]
	if menorx>d[0]:
		menorx = d[0]
	
	menory = a[1]
	
	if menory>b[1]:
		menory = b[1]
	if menory>c[1]:
		menory = c[1]
	if menory>d[1]:
		menory = d[1]
