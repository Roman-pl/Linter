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
		elif s.find('+ ') >= 1:
			s = s.replace('+ ','')
			a = False
		elif s.find(' +') >= 1:
			s = s.replace(' +','')
			a = False
	return a

def check_equally (s):
	a = True
	while s.find('=') >= 1:
		if s.find(' = ') >= 1:
			a = True
			s = s.replace(' = ','')
		if s.find('=') >= 1:
			s = s.replace('=','')
			a = False
		elif s.find('= ') >= 1:
			s = s.replace('= ','')
			a = False
		elif s.find(' =') >= 1:
			s = s.replace(' =','')
			a = False
	return a

def check_or (s):
	a = True
	while s.find(')or(') or s.find(')or (') or s.find(') or(') >= 1:
		if s.find(') or (') >= 1:
			a = True
			s = s.replace(') or (','')
		if s.find(')or(') >= 1:
			s = s.replace(')or(','')
			a = False
		elif s.find(')or (') >= 1:
			s = s.replace(')or (','')
			a = False
		elif s.find(') or(') >= 1:
			s = s.replace(') or(','')
			a = False
	return a

def check_and (s):
	a = True
	while s.find(')and(') or s.find(')and (') or s.find(') and(') >= 1:
		if s.find(') and (') >= 1:
			a = True
			s = s.replace(') and (','')
		if s.find(')and(') >= 1:
			s = s.replace(')and(','')
			a = False
		elif s.find(')and (') >= 1:
			s = s.replace(')and (','')
			a = False
		elif s.find(') and(') >= 1:
			s = s.replace(') and(','')
			a = False
	return a

def check_more_equally (s):
	a = True
	while s.find('>=') >= 1:
		if s.find(' >= ') >= 1:
			a = True
			s = s.replace(' >= ','')
		if s.find('>=') >= 1:
			s = s.replace('>=','')
			a = False
		elif s.find('>= ') >= 1:
			s = s.replace('>= ','')
			a = False
		elif s.find(' >=') >= 1:
			s = s.replace(' >=','')
			a = False
	return a

def check_more_equally (s):
	a = True
	while s.find('<=') >= 1:
		if s.find(' <= ') >= 1:
			a = True
			s = s.replace(' <= ','')
		if s.find('<=') >= 1:
			s = s.replace('<=','')
			a = False
		elif s.find('<= ') >= 1:
			s = s.replace('<= ','')
			a = False
		elif s.find(' <=') >= 1:
			s = s.replace(' <=','')
			a = False
	return a

with open("example.txt", "r") as file:
	line = list(file)
	print(line,file)
	flag = check_plus(line[i])
for i in range(len(line)):
	flag = check_plus((line[i]))
	flag = check_or(line[i])
	flag = check_and(line[i])
	flag = check_more_equally(line[i])
	flag = check_less_equally(line[i])
	if flag == False:
		FlagGlobal = False
with open("check_list.txt", "a") as file:
    print(FlagGlobal, file=file)