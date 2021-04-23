# -*- coding: utf-8 -*-
"""My Shiftcode.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l2Ab0jXvgqNwGn-ViY23kYzNQl4-Gh7t
"""

#-----------------------Start--------------------------#
# -*- coding: utf-8 -*-
"""My ShiftCode.ipynb

# **SHIFTCODEPYTHO**
"""

#selection between three functions 
def cond():
    selection = menu()
    print('\n')
    if selection == 1:
        print(make_a_code())
        print('\n')
        cond()
    elif selection ==2:
        print(decode_a_message())
        print('\n')
        cond()
    elif selection==3:
        print('Thank-You')
    elif selection not in (1,2,3):
        print('Enter a valid number')
        print('\n')
        cond()

#returning value after selection

def menu():
    return int(input('''SHIFTCODE
    -----------
    1) Make a code
    2) Decode a message
    3) Quit
    Enter your selection:
    '''))
def enc_let(x , num):
    asc = ord(x)+num
    if asc<=122:
        return chr(asc)
    else:
        return chr(asc-26)
def dec_let(x , num):
    asc = ord(x)-num
    if asc>=97:
        return chr(asc)
    else:
        return chr(asc+26)
#Part 1 

def make_a_code():
    msg = input("Enter the msg (only lower case)   ").strip()
    if msg.isalpha()!=True:
        msg= input('Please enter only letters'   ).strip()
    if msg.islower()==False:
        msg = input("Please enter in lower case"  ).strip()
    num=int(input("Enter the number   "))
    encoded_msg = ''
    for x in msg:
        encoded_msg = encoded_msg + enc_let(x , num)    
    return encoded_msg

#Part 2

def decode_a_message():
    code = input("Enter the code (only lower case)   ").strip()
    if code.isalpha()!=True:
        code = input("Please enter letters only    ").strip()
    if code.islower()==False:
        code = input("Please enter in lower case"  ).strip()
    num=int(input("Enter the number   "))
    decoded_msg = ''
    for x in code:
        decoded_msg = decoded_msg + dec_let(x , num)    
    return decoded_msg
cond()

#------------------End----------------------#

64