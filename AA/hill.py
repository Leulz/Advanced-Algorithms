#original message: xmrkrbdjtizcqdqnbvvuhxlnylfolwwypozhnhlpjdnaprtn
#decoded with caesar key 3: ujohoyagqfwznankyssreuikviclittvmlwekeimgakxmoqk
#encoded with caesar key 3: apunuegmwlcftgtqeyyxkaoqboirozzbsrckqkosmgqdsuwq


string = raw_input()

x = []
matrix = [[18,0,1],[4,3,14],[17,8,0]]
ans = []

for i in range(len(string)):
	if len(x)<3:
		x.append(ord(string[i])-97)
	else:
		temp = []
		
		for j in range(3):
			temp_int = 0
			for m in range(3):
				temp_int+=matrix[j][m]*x[m]
			temp.append(temp_int)
		ans.extend(temp)
		x = []
		temp = []

print ''.join([chr((h%26)+97) for h in ans])
