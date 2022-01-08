import tkinter as tk
from tkinter import filedialog
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
    s2 = s
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
    s2 = s
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
    s2 = s
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
    s2 = s
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
    s2 = s
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
    s2 = s
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
    s2 = s
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
    s2 = s
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
    s2 = s
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
    s2 = s
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
    s2 = s
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
        s = ''.join(b)
    s = ''.join(b)
    return s

print("проверяемый")
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

file = open(file_path,"r")
line = list(file)
file.close()

print("настройки")
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

file = open(file_path,"r")
l = list(file)
file.close()

for i in range(len(l)):
    if l[i].find('Tab')>-1:
        s = l[i]
        z.append(int(s[6]))
    else:
        z.append(l[i][5:len(l[i])-2].replace("'",""))

for i in range(len(line)):
    line[i] = string(line[i])
    if line[i].find('///') > -1:
        a = line[i].split('///')
        line[i] = a[0]
    if line[i].find('//') > -1:
        a = line[i].split('//')
        line[i] = a[0]

flag = False
for i in range(len(line)):
    s = ''.join(line[i])
    if s.find('{') > -1:
        x = s.find('{') 
        flag = True
    if flag == True:
        s = list(s)
        for x in range(x,len(s)):
            if s[x] == '}':
                flag = False
                s[x] = '' 
                break
            else:
                s[x] = '' 
        line[i] = ''.join(s)
        x = 0
        
count = 0
a = []

for i in range(len(line)):
    s = ''.join(line[i])
    if s.find('end') == -1:
        if s.startswith(' '*4*count*z[0]) == False: 
            FlagGlobal = False
            
    if s.find('begin') > -1:
        count += 1
    if s.find('end') > -1:
        count += -1

    if s.find('repeat') > -1:
        count += 1
    if s.find('until') > -1:
        count += -1
        
    if s.find('if') > -1:
        a = s.split('then')
        if  a[1].isspace() == False:
            FlagGlobal = False

for i in range(len(line)):
    s = (line[i]).lower()
    if s.find('for') > -1:
        if s.find('do') == -1:
            FlagGlobal = False
    if s.find('for') > -1:
        line[i+1] =  line[i+1].lower()
        if line[i+1].find("begin") == -1:
            if line[i+1].startswith("    ") == -1:
                FlagGlobal = False

for i in range(len(line)):
    s = (line[i]).lower()
    if s.find('whiles') > -1:
        line[i+1] =  line[i+1].lower()
        if line[i+1].find("begin") == -1:
            if line[i+1].startswith("    ") == -1:
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
        if check_dvsn(s,z[10]) == False:
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