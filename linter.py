import tkinter as tk
from tkinter import messagebox
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
c = 1
ss = ''
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
    s2 = s.lower()
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
    s2 = s.lower()
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

root = tk.Tk()
root.withdraw()
messagebox.showinfo("Linter", "???????????????? ???????? ?????????????? ???? ???????????? ??????????????????")
file_path1 = filedialog.askopenfilename()

file = open(file_path1,"r")
line = list(file)
file.close()

root = tk.Tk()
root.withdraw()
messagebox.showinfo("Linter", "???????????????? ?????????? ???????? ?? ?????????????????????? ???? ???????????? ??????????????????")
file_path2 = filedialog.askopenfilename()

file = open(file_path2,"r")
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
c = 1
for i in range(len(line)):
    ?? = c + 1
    s = (line[i].lower())
    if s.find('end') == -1:
        if s.startswith(' '*4*count*z[0]) == False: 
            FlagGlobal = False
            ss += str(c) + ','
            
    if s.find('begin') > -1 or s.find("record")  > -1:
        count += 1
    if s.find('end') > -1:
        count += -1

    if s.find('repeat') > -1:
        count += 1
    if s.find('until') > -1:
        count += -1
        
    if s.find('if') > -1:
        if s.find('then') > -1:
            a = s.split('then')
            if a[1].isspace() == False:
                FlagGlobal = False
                ss += str(c) + ','
        else:
            FlagGlobal = False

    if s.find(';') > -1:
        a = s.split(';')
        if  a[1].isspace() == False:
            FlagGlobal = False
            ss += str(c) + ','

    if s.find('var') > -1:
        a = s.split('var')
        if  a[1].isspace() == False:
            FlagGlobal = False
            ss += str(c) + ','

for i in range(len(line)):
    s = (line[i]).lower()
    if s.find('for') > -1:
        if s.find('do') == -1:
            FlagGlobal = False
            ss += str(c) + ','

    if s.find('for') > -1:
        line[i+1] =  line[i+1].lower()
        if line[i+1].find("begin") == -1:
            if line[i+1].startswith(" "*4*z[0]) == -1:
                FlagGlobal = False
                ss += str(c) + ','

for i in range(len(line)):
    s = (line[i]).lower()
    if s.find('while') > -1:
        line[i+1] =  line[i+1].lower()
        if line[i+1].find("begin") == -1:
            if line[i+1].startswith(" "*4*z[0]) == -1:
                FlagGlobal = False
                ss += str(c) + ','
count = 0
c = 1
for i in range(len(line)):
    c += 1
    s = ''.join(line[i])
    if s.find('+') > -1:
        if check_plus(s,z[1]) == False:
            FlagGlobal = False
            ss += str(c) + ','
    if s.find('and') > -1:
        if check_and(s) == False:
            FlagGlobal = False
            ss += str(c) + ','
    if s.find('=') > -1:
        if check_eq(s,z[3]) == False:
            FlagGlobal = False
            ss += str(c) + ','
    if s.find('<=') > -1:
        if check_ls_eq(s,z[7]) == False:
            FlagGlobal = False
            ss += str(c) + ','
    if s.find('>=') > -1:
        if check_mr_eq(s,z[6]) == False:
            FlagGlobal = False
            ss += str(c) + ','
    if s.find(':=') > -1:
        if check_assg(s,z[9]) == False:
            FlagGlobal = False
            ss += str(c) + ','
    if s.find('/') > -1:
        if check_dvsn(s,z[10]) == False:
            FlagGlobal = False
            ss += str(c) + ','
    if s.find('or') > -1:
        if check_or(s) == False:
            FlagGlobal = False
            ss += str(c) + ','
    if s.find('<') > -1:
        if check_less(s,z[5]) == False:
            FlagGlobal = False
            ss += str(c) + ','
    if s.find('>') > -1:
        if check_more(s,z[4]) == False:
            FlagGlobal = False
            ss += str(c) + ','

with open("check_list.txt", "a") as file:
    if FlagGlobal == False:
        print('"',file_path1,'"',"?????????????? ???? ?????????????????????? ?? ????????????:",ss,file = file)
    else:
        print('"',file_path1,'"',"???? ?????????????????????? ???? ??????????????",file = file)
print(ss)