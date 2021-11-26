flag = True
FlagGlobal = True

def check_plus(s):
	for i in range(len(s)):
		if s[i] = '+':
			if s[i]+s[i+1] == '+ ' and s[i-1]+s[i] == ' +' and s[i+2] != ' ' and s[i-2] != ' ':
				return True
			else:
				return False

def check_more(s):
	for i in range(len(s)):
		if s[i] = '>':
			if s[i]+s[i+1] == '> ' and s[i-1]+s[i] == ' >' and s[i+2] != ' ' and s[i-2] != ' ':
				return True
			else:
				return False

def check_less(s):
	for i in range(len(s)):
		if s[i] = '<':
			if s[i]+s[i+1] == '< ' and s[i-1]+s[i] == ' <' and s[i+2] != ' ' and s[i-2] != ' ':
				return True
			else:
				return False

with open("example.txt", "r") as file:
	line = list(file)
for i in range(len(line)):
	if line[i].find('+'):
		if check_plus(s) == False:
			FlagGlobal = False
	if line[i].find('>'):
		if check_more(s) == False:
			FlagGlobal = False

with open("check_list.txt", "a") as file:
    print(FlagGlobal, file=file)
#в следущий раз до делаю все сравнительные операции и разберусь что там с минусом как с ним взаимодействовать + комментарии