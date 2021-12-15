flag = True
FlagGlobal = True
a = []
b = []
z = []
x = []
n = 0
s = ''
s2 =''
b2 =''
def check_plus(s,s1):
    flag2 = True
    flag = True
    s2 = ' '.join(s.split(' '))
    if s != s2:
        flag2 = False
    else:
        s2 = s2.replace(s1,'')
        if s2.find('+') > -1:
            flag = False
    if flag2 == True and flag == True:
        return True
    else:
        return False

def check_mines(s,s1):
    flag2 = True
    flag = True
    s2 = ' '.join(s.split(' '))
    if s != s2:
        flag2 = False
    else:
        s2 = s2.replace(s1,'')
        if s2.find('-') > -1:
            flag = False
    if flag2 == True and flag == True:
        return True
    else:
        return False

def check_dvsn(s,s1):
    flag2 = True
    flag = True
    s2 = ' '.join(s.split(' '))
    if s != s2:
        flag2 = False
    else:
        s2 = s2.replace(s1,'')
        if s2.find('/') > -1:
            flag = False
    if flag2 == True and flag == True:
        return True
    else:
        return False        

def check_more(s,s1):
    flag = True
    flag2 = True
    s = s.replace('>=','')
    s = s.replace('<=','')
    s = s.replace('<>','')
    s2 = ' '.join(s.split(' '))
    if s != s2:
        flag2 = False
    else:
        s2 = s2.replace(s1,'')
        if s2.find('>') > -1:
            flag = False
    if flag2 == True and flag == True:
        return True
    else:
        return False

def check_less(s,s1):
    flag = True
    flag2 = True
    s = s.replace('>=','')
    s = s.replace('<=','')
    s = s.replace('<>','')
    s2 = ' '.join(s.split(' '))
    if s != s2:
        flag2 = False
    else:
        s2 = s2.replace(s1,'')
        if s2.find('<') > -1:
            flag = False
    if flag2 == True and flag == True:
        return True
    else:
        return False
    
def check_mr_eq(s,s1):
    flag = True
    flag2 = True
    s2 = ' '.join(s.split(' '))
    if s != s2:
        flag2 = False
    else:
        s2 = s2.replace(s1,'')
        if s2.find('>=') > -1:
            flag = False
    if flag == True and flag2 == True:
        return True
    else:
        return False

def check_assg(s,s1):
    flag = True
    flag2 = True
    s2 = ' '.join(s.split(' '))
    if s != s2:
        flag2 = False
    else:
        s2 = s2.replace(s1,'')
        if s2.find(':=') > -1:
            flag = False
    if flag == True and flag2 == True:
        return True
    else:
        return False

def check_ls_eq(s,s1):
    flag = True
    flag2 = True
    s2 = ' '.join(s.split(' '))
    if s != s2:
        flag2 = False
    else:
        s2 = s2.replace(s1,'')
        if s2.find('<=') > -1:
            flag = False
    if flag == True and flag2 == True:
        return True
    else:
        return False

def check_eq(s,s1):
    flag = True
    flag2 = True
    s = s.replace('>=','')
    s = s.replace('<=','')
    s2 = ' '.join(s.split(' '))
    if s != s2:
        flag2 = False
    else:
        s2 = s2.replace(s1,'')
        if s2.find('=') > -1:
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
    while s.find('"') > -1:
        a = s.find('"')
        b = list(s)
        b[a] = '`'
        s = ''.join(b)
        c = s.find('"')
        for i in range(a,c+1):
            b[i] = ''
        s = ''.join(b)
    s = ''.join(b)
    return s

with open("example.txt", "r") as file:
    line = list(file)

with open("settings.ini", "r") as file:
    z = list(file)

for i in range(len(z)):
    if z[i].find('Tab')  > -1:
       x = z[i].split(' ')
       z[i] = x[2]
    else:
        x = z[i].split('-')
        z[i] = x[2].replace("'","")

    if  z[i].find('-') > -1:
        s = z[i].replace('-','',2)
        z[i] = s.replace("'",'')

for i in range(len(line)):
    line[i] = string(line[i])
    if line[i].find('///') > -1:
        a = line[i].split('///')
        line[i] = a[0]
    if line[i].find('//') > -1:
        a = line[i].split('//')
        line[i] = a[0]

for i in range(len(line)):
    s = ''.join(line[i])
    if s.find('{') > -1:
        x = s.find('{') 
        flag = True
        while flag == True:
            s = list(s)
            if s[x] == '}':
                flag = False
            s[x] = ''
            x += 1
            line[i] = s

count = 0
a = []

for i in range(len(line)):
    s = ''.join(line[i])
    if s.find('end') == -1:
        if s.startswith('   '*count*z[0]) == False: 
            FlagGlobal = False
            
    if s.find('begin') > -1:
        count += 1
    if s.find('end') > -1:
        count += -1
        
    if s.find('if') > -1:
        a = s.split('then')
        if  a[1].isspace() == False:
            FlagGlobal = False

for i in range(len(line)):
    s = ''.join(line[i])
    if s.find('+') > -1:
        if check_plus(s,z[1]) == False:
            FlagGlobal = False
    if s.find('and') > -1:
        if check_and(s) == False:
            FlagGlobal = False
    if s.find('=') > -1:
        if check_eq(s,z[3]) == False:
            FlagGlobal = False
    if s.find('<=') > -1:
        if check_ls_eq(s,z[7]) == False:
            FlagGlobal = False
    if s.find('>=') > -1:
        if check_mr_eq(s,z[6]) == False:
            FlagGlobal = False
    if s.find(':=') > -1:
        if check_assg(s,z[9]) == False:
            FlagGlobal = False
    if s.find('/') > -1:
        if check_dvsn(s,z[9]) == False:
            FlagGlobal = False
    if s.find('or') > -1:
        if check_or(s) == False:
            FlagGlobal = False
    if s.find('<') > -1:
        if check_less(s,z[5]) == False:
            FlagGlobal = False
    if s.find('>') > -1:
        if check_more(s,z[4]) == False:
            FlagGlobal = False

with open("check_list.txt", "a") as file:
    print(FlagGlobal, file=file)