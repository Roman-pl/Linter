flag = True
FlagGlobal = True
a = []
b = []
z = []
n = 0
s2 =''
b2 =''
def check_plus(s):
    flag2 = True
    flag = True
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

def check_mines(s):
    flag2 = True
    flag = True
    s2 = ' '.join(s.split(' '))
    if s != s2:
        flag2 = False
    for i in range(len(s2)):
        if s2[i] == '-':
            if s2[i]+s2[i+1] == '- ' and s2[i-1]+s2[i] == ' -' and s2[i+2] != ' ' and s2[i-2] != ' ':
                flag = True
            else:
                flag = False
    if flag2 == True and flag == True:
        return True
    else:
        return False

def check_dvsn(s):
    flag2 = True
    flag = True
    s2 = ' '.join(s.split(' '))
    if s != s2:
        flag2 = False
    for i in range(len(s2)):
        if s2[i] == '/':
            if s2[i]+s2[i+1] == '/ ' and s2[i-1]+s2[i] == ' /' and s2[i+2] != ' ' and s2[i-2] != ' ':
                flag = True
            else:
                flag = False
    if flag2 == True and flag == True:
        return True
    else:
        return False        

def check_more(s):
    flag = True
    flag2 = True
    s = s.replace('>=','')
    s = s.replace('<=','')
    s = s.replace('<>','')
    s2 = ' '.join(s.split(' '))
    if s != s2:
        flag2 = False
    else:
        for i in range(len(s2)):
            if s2[i] == '>':
                if s2[i]+s2[i+1] == '> ' and s2[i-1]+s2[i] == ' >' and s2[i+2] != ' ' and s2[i-2] != ' ':
                    flag = True
                else:
                    flag = False
    if flag2 == True and flag == True:
        return True
    else:
        return False

def check_less(s):
    flag = True
    flag2 = True
    s = s.replace('>=','')
    s = s.replace('<=','')
    s = s.replace('<>','')
    s2 = ' '.join(s.split(' '))
    if s != s2:
        flag2 = False
    else:
        for i in range(len(s2)):
            if s2[i] == '<':
                if s2[i]+s2[i+1] == '< ' and s2[i-1]+s2[i] == ' <' and s2[i+2] != ' ' and s2[i-2] != ' ':
                    flag = True
                else:
                    flag = False
    if flag2 == True and flag == True:
        return True
    else:
        return False
    
def check_mr_eq(s):
    flag = True
    flag2 = True
    s2 = ' '.join(s.split(' '))
    if s != s2:
        flag2 = False
    else:
        s2 = s2.replace(' >= ','')
        if s2.find('>=') > -1:
            flag = False
    if flag == True and flag2 == True:
        return True
    else:
        return False

def check_assg(s):
    flag = True
    flag2 = True
    s2 = ' '.join(s.split(' '))
    if s != s2:
        flag2 = False
    else:
        s2 = s2.replace(' := ','')
        if s2.find(':=') > -1:
            flag = False
    if flag == True and flag2 == True:
        return True
    else:
        return False

def check_ls_eq(s):
    flag = True
    flag2 = True
    s2 = ' '.join(s.split(' '))
    if s != s2:
        flag2 = False
    else:
        s2 = s2.replace(' <= ','')
        if s2.find('<=') > -1:
            flag = False
    if flag == True and flag2 == True:
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
    else:
        for i in range(len(s2)):
            if s2[i] == '=':
                if s2[i]+s2[i+1] == '= ' and s2[i-1]+s2[i] == ' =' and s2[i+2] != ' ' and s2[i-2] != ' ':
                    flag = True
                else:
                    flag = False
    if flag2 == True and flag == True:
        return True
    else:
        return False

def check_or(s):
    flag = True
    flag2 = True
    s2 = ' '.join(s.split(' '))
    if s != s2:
        flag2 = False
    a = s2.find('or')
    if a > -1:
        if s2[a-1] == ' ' and  s2[a+2] == ' ':
            flag = True
        elif s2[a-1] == ')' and  s2[a+2] == '(':
            flag = False
    if flag2 == True and flag == True:
        return True
    else:
        return False

def check_and(s):
    flag = True
    flag2 = True
    s2 = ' '.join(s.split(' '))
    if s != s2:
        flag2 = False
    a = s2.find('and')
    if a > -1:
        if s2[a-1] == ' ' and  s2[a+2] == ' ':
            flag = True
        elif s2[a-1] == ')' and  s2[a+2] == '(':
            flag = False
    if flag2 == True and flag == True:
        return True
    else:
        return False

def string(s):
    b = list(s)
    while s.find("'") > -1:
        a = s.find("'")
        b = list(s)
        b[a] = "`"
        s = "".join(b)
        c = s.find("'")
        for i in range(a,c+1):
            b[i] = ''
        s = "".join(b)
    s = "".join(b)
    return s

with open("example.txt", "r") as file:
    line = list(file)
for i in range(len(line)):
    line[i] = string(line[i])
    if line[i].find('///') > -1:
        a = line[i].split('///')
        line[i] = a[0]
    if line[i].find('//') > -1:
        a = line[i].split('//')
        line[i] = a[0]

for i in range(len(line)):
    b.append(line[i])
line = ' '.join(b)
while line.find("{") > -1:
        n = line.find("{")
        z = list(line)
        line = "".join(z)
        c = line.find("}")
        for i in range(n,c+1):
            z[i] = ''
        s = "".join(z)
    line = "".join(z)

if line.find('+'):
    if check_plus(line) == False:
        FlagGlobal = False
if line.find('and'):
    if check_and(line) == False:
        FlagGlobal = False
if line.find('='):
    if check_eq(line) == False:
        FlagGlobal = False
if line.find('<='):
    if check_ls_eq(line) == False:
        FlagGlobal = False
if line.find('>='):
    if check_mr_eq(line) == False:
        FlagGlobal = False
if line.find(':='):
    if check_assg(line) == False:
        FlagGlobal = False
if line.find('\\'):
    if check_dvsn(line) == False:
        FlagGlobal = False
if line.find('or'):
    if check_or(line) == False:
        FlagGlobal = False
if line.find('<'):
    if check_less(line) == False:
        FlagGlobal = False
if line.find('>'):
    if check_more(line) == False:
        FlagGlobal = False

with open("check_list.txt", "a") as file:
    print(FlagGlobal, file=file)
#в следущий раз до делаю все сравнительные операции и разберусь что там с минусом как с ним взаимодействовать + комментарии