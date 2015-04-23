def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

while True:
	n = long(raw_input())
	
	if n == 0:
		break
	
	if n==1:
		print 'yes'
	elif is_square(n):
		print 'yes'
	else:
		print 'no'
