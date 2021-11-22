s=input('введите строку ')
def test_check (s):
	flag = False
	n=0
	for i in range(len(s)):
		n += 1 
		if s[i] == ' ':
			if len(s) - n + 1 > 3:
		 		break
			else:
				if s[i]+s[i+1]+s[i+2] == ' + ':
					flag = True
				else:
					flag = False
	print(flag)				
test_check(s)