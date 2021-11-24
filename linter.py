
def test_check (s):
	try:
		if s.rindex(' + ') == True:
			with open("check_list.txt", "a") as file:
				print('True',file=file)
	except ValueError:
		with open("check_list.txt", "a") as file:
	 		print('False',file=file)
s = input('введите строку ')				
test_check(s)

