# -*- coding: utf-8 -*-
"""My Domu Password .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18LeAQKu4lMNm0FEcnmAG-MziXVmeyKmM
"""

#Name = Domendra Sahu
#Email =  domendrasahu911@gmail.com

import csv
f =open("uid_password.csv", "a")

def pswd():
    p = input('''Enter the new password::-
    
    1) It should have at least 8 characters.

    2) It should include both upper and lower case letters.

    3) It should include numbers.

    4) It should include at least one special character such as !, £, $, %, &, <, * or @.

    DON'T do the following:

    1) DON'T include all or part of your username, first name, or last name.

    2) DON'T use your favorite sport as a password — "baseball" and "football" are among the top 10 worst passwords, and "hockey," "soccer" and "golfer" are in the top 100.

    3) DON'T make obvious choices like your nickname, birthdate, spouse name, pet name, make/model of car, or favorite expression.

    4) DON'T share your password with anyone.

    5) DON'T use blank spaces in your password.

    6) DON'T use a word contained in English or foreign language dictionaries, spelling lists or commonly digitized texts such as the Bible or an encyclopedia.

    7) DON'T use an alphabet sequence (lmnopqrst), a number sequence (12345678) or a keyboard sequence (qwertyuop).


  ''' )
    l , u , lo , nm , cr = 0,0,0,0,0
    if len(p) >= 8:
        l =1
    for i in p:                 #code contributed by DomendraSahu
        if i.isupper():
            u = 1
        elif i.islower():
            lo=1
        elif i in ['1','2','3','4','5','6','7','8','9','0']:
            nm= 1
        elif i in ["!", "£", "$","%", "&", "<", "*", "@"]:
            cr= 1
    score = l+u+lo+nm+cr
 #code contributed by DomendraSahu

    if score in (0,1,2):
        print("Your Password is Weak password \n Please try again")
        pswd()
    elif score == 3 or score == 4:
        print("This password could be improved,Please try again.")
        opt = input('Want to try again please select (y,n):  ').lower()
        if opt=='y':
            return pswd()
        else:
            return p+'\n'
    else:
        print("Your password is strong password")
        return p+'\n'

def get_id():
    new_id = input("Create/Enter a new username:   ")
    f =  open("uid_password.csv", "r")
    tmp = list(csv.reader(f))
    u_id = []
    for i in tmp:
        u_id.append(i[0])
    if new_id not in u_id:
        f =open("uid_password.csv", "a")
        newrecord = new_id + "," + pswd()
        f.write(str(newrecord))
        f.close()
        print("Your Id has been created")
    else:
        f.close()
        print("This username already exixts")

#code contributed by DomendraSahu

def cng_pswd():
    u_id = input("Enter the username:   ")
    f=open("uid_password.csv", "r")
    tmp = list(csv.reader(f))
    present = 0
    for i in range(len(tmp)):
        if u_id ==tmp[i][0]:
            new_pwd = input('Please enter new password:  ').strip()
            tmp[i][1]=new_pwd
            print('password successfully changed')
            present = 1
            f = open('uid_password.csv','w')
            w = csv.writer(f)
            w.writerows(tmp)
    if present==0:
        print('Invalid username ')        
              

#code contributed by DomendraSahu

def display_uid():
    f = open("uid_password.csv","r")
    tmp = list(csv.reader(f))
    u_id = []
    for i in tmp:
        u_id.append(i[0])
    f.close()
    return u_id

print("PASSWORD")

#code contributed by DomendraSahu

while True:
    print('''   1) Create a new User Identity 
    2) Change your old password
    3) Display all User Identities 
    4) Quit
    ''')
    selection= int(input("Enter the choice: "))
    if selection == 1:
        print(get_id())
        exit()
    elif selection == 2:
        print(cng_pswd())
        exit()
    elif selection == 3:
        print("List of Usernames :::")
        print(display_uid())                
        exit()
    elif selection == 4:             
        exit()
    
    else:
        print("Please enter a valid choice")

1