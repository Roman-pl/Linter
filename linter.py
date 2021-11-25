flag = True
FlagGlobal = True

def check_plus (s):
	a = True
	while s.find('+') > -1:
		if s.find(' + ') > -1:
			a = True
			s = s.replace(' + ','')
		if s.find('+') >= 1:
			s = s.replace('+','')
			a = False

def check_equally (s):
	a = True
	while s.find('=') > -1:
		if s.find(' = ') >= 1:
			a = True
			s = s.replace(' = ','')
		if s.find('=') >= 1:
			s = s.replace('=','')
			a = False
	return a

def check_or (s):
	a = True
	while s.find('or') > -1:
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
	while s.find(')and(') or s.find(')and (') or s.find(') and(') > -1:
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
	while s.find('>=') > -1:
		if s.find(' >= ') >= 1:
			a = True
			s = s.replace(' >= ','')
		if s.find('>=') >= 1:
			s = s.replace('>=','')
			a = False
	return a

def check_more_equally (s):
	a = True
	while s.find('<=') > -1:
		if s.find(' <= ') >= 1:
			a = True
			s = s.replace(' <= ','')
		if s.find('<=') >= 1:
			s = s.replace('<=','')
			a = False
		return a
	return a

with open("example.txt", "r") as file:
	line = list(file)
for i in range(len(line)):
	if line[i].find('+') > -1:
		flag = check_plus((line[i]))
	elif line[i].find('<=') > -1:
		flag = check_less_equally(line[i])
	elif line[i].find('>=') > -1:
		flag = check_more_equally(line[i])
	elif line[i].find(')or(') or line[i].find(') or(') or  line[i].find(')or (') > -1:
		flag = check_or(line[i])
	else:
		flag = check_and(line[i])
	if flag == False:
		FlagGlobal = False
with open("check_list.txt", "a") as file:
    print(FlagGlobal, file=file)
#в следущий раз до делаю все сравнительные операции и разберусь что там с минусом как с ним взаимодействовать + комментарии