flag = True
FlagGlobal = True

def check_plus(s):
	flag2 = True
	s2 = ' '.join(s.split(' '))
	if s != s2:
		flag2 = False
	for i in range(len(s2)):
		if s2[i] == '+':
			if s2[i]+s2[i+1] == '+ ' and s2[i-1]+s2[i] == ' +' and s2[i+2] != ' ' and s2[i-2] != ' ':
				flag = True
			else:
				flag = False
	if flag2 == True and flag == True:
		return True
	else:
		return False

# def check_more(s):
	
# def check_less(s):
	

def check_mr_eq(s):
	flag2 = True
	s2 = ' '.join(s.split(' '))
	if s != s2:
		flag2 = False
		
	if flag2 == True and flag == True:
		return True
	else:
		return False

def check_ls_eq(s):
	flag2 = True
	s2 = ' '.join(s.split(' '))
	if s != s2:
		flag2 = False

	if flag2 == True and flag == True:
		return True
	else:
		return False

def check_eq(s):
	flag = True
	flag2 = True
	s = s.replace('>=','')
	s = s.replace('<=','')
	s2 = ' '.join(s.split(' '))
	if s != s2:
		flag2 = False
	for i in range(len(s2)):
		if s[i] == '=':
			if s[i]+s[i+1] == '= ' and s[i-1]+s[i] == ' =' and s[i+2] != ' ' and s[i-2] != ' ':
				flag = True
			else:
				flag = False
	if flag2 == True and flag == True:
		return True
	else:
		return False

with open("example.txt", "r") as file:
	line = list(file)
for i in range(len(line)):
	if line[i].find('+'):
		if check_plus(line[i]) == False:
			FlagGlobal = False

with open("check_list.txt", "a") as file:
    print(FlagGlobal, file=file)
#в следущий раз до делаю все сравнительные операции и разберусь что там с минусом как с ним взаимодействовать + комментарии