flag = True
FlagGlobal = True

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

with open("example.txt", "r") as file:
    line = list(file)
for i in range(len(line)):
    if line[i].find('+'):
        if check_plus(line[i]) == False:
            FlagGlobal = False
    if line[i].find('and'):
        if check_and(line[i]) == False:
            FlagGlobal = False
    if line[i].find('='):
        if check_eq(line[i]) == False:
            FlagGlobal = False
    if line[i].find('<='):
        if check_ls_eq(line[i]) == False:
            FlagGlobal = False
    if line[i].find('>='):
        if check_mr_eq(line[i]) == False:
            FlagGlobal = False
    if line[i].find(':='):
        if check_assg(line[i]) == False:
            FlagGlobal = False
    if line[i].find('\\'):
        if check_dvsn(line[i]) == False:
            FlagGlobal = False
    if line[i].find('or'):
        if check_or(line[i]) == False:
            FlagGlobal = False
    if line[i].find('<'):
        if check_less(line[i]) == False:
            FlagGlobal = False
    if line[i].find('>'):
        if check_more(line[i]) == False:
            FlagGlobal = False

with open("check_list.txt", "a") as file:
    print(FlagGlobal, file=file)
#в следущий раз до делаю все сравнительные операции и разберусь что там с минусом как с ним взаимодействовать + комментарии