import math

actual = list(raw_input())

received = list(raw_input())

actual_plus = 0
actual_minus = 0

received_plus = 0
received_minus = 0
fuzzy = 0

for i in actual:
	if i=='+':
		actual_plus += 1
	elif i=='-':
		actual_minus += 1
		
for i in received:
	if i=='+':
		received_plus += 1
	elif i=='-':
		received_minus += 1	
	else:
		fuzzy += 1

if received_plus>actual_plus or received_minus>actual_minus:
	print 0.0
elif received_minus==actual_minus and received_plus==actual_plus:
	print 1.0
else:
	diff_plus = actual_plus-received_plus
	diff_minus = actual_minus-received_minus
	
	total = pow(2,fuzzy)
	
	resp = math.factorial(fuzzy)/(math.factorial(fuzzy-diff_plus)*math.factorial(diff_plus))/float(total)
	print resp
