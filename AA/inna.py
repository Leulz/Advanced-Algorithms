n = int(raw_input())
temp = []

for i in range(n):
	resp = []
	temp = [x for x in raw_input()]
	contador = 0
	ocorrencias = 0
	for j in range(6):
		if temp[j]=="X" or temp[j+6]=="X":
			resp.append("1x12")			
			ocorrencias+=1
			break
	for j in range(6):
		if temp[j]==temp[j+6] and temp[j]=="X":
			resp.append("2x6")
			ocorrencias+=1
			break
	for j in range(4):
		if temp[j]==temp[j+4] and temp[j]==temp[j+8] and temp[j]=="X":
			resp.append("3x4")
			ocorrencias+=1
			break
	for j in range(3):
		if temp[j]==temp[j+3] and temp[j]==temp[j+6] and temp[j]==temp[j+9] and temp[j]=="X":
			resp.append("4x3")
			ocorrencias+=1
			break
	for j in range(2):
		if temp[j]==temp[j+2] and temp[j]==temp[j+4] and temp[j]==temp[j+6] and temp[j]==temp[j+8] and temp[j]==temp[j+10] and temp[j]=="X":
			resp.append("6x2")
			ocorrencias+=1
			break
	for j in range(12):
		if temp[j]!="X":
			break
		contador+=1
	if contador==12:
		resp.append("12x1")
		ocorrencias+=1
	print "%d %s" % (ocorrencias, ' '.join(resp))
