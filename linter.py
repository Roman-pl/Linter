flag = True
FlagGlobal = True
def check_plus (s):
	a = True
	while s.find('+') >= 1:
		if s.find(' + ') >= 1:
			a = True
			s = s.replace(' + ','')
		if s.find('+') >= 1:
			s = s.replace('+','')
			a = False
	return a

def check_or (s):
	a = True
	while s.find(')or(') >= 1:
		if s.find(') or (') >= 1:
			a = True
			s = s.replace(') or (','')
		if s.find(')or(') >= 1:
			s = s.replace(')or(','')
			a = False
	return a

with open("example.txt", "r") as file:
	line = list(file)
	print(line,file)
for i in range(len(line)):
	flag = check_plus(line[i])
	flag = check_or(line[i])
	if flag == False:
		FlagGlobal = False
with open("check_list.txt", "a") as file:
    print(FlagGlobal, file=file)