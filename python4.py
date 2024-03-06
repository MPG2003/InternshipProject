import random #IMPORTED RANDOM TO PRINT RANDOM CHARACTERS FROM LOWE, UPPER,NUMBER AND SYMBOLS
upper_str="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_str=upper_str.lower() #LOWER() CONVERS CAPITAL LETTER TO SMALL
number="1234567890"
special_char="!@#$%^&*(){}[]'|\\:;?/>.<,"
upper,lower,num,sym=True,True,True,True
#IF YOU DON'T NEED SYMBOLS OR ALPHABETS OR NUMBERS IN THE PASSWORD SIMPLY TYPE FALSE TO ITS CORRESPONDING
passw=""
if(upper):
    passw=passw+upper_str
if(lower):
    passw=passw+lower_str
if(num):
    passw=passw+number
if(sym):
    passw=passw+special_char

#passw=upper_str+lower_str+number+special_char (EVERYTHING GOES AS THE PASSWORD)

l=int(input("enter length of the password: ")) # USER INPUT LENGTH OF THE PASSWORD
n=int(input("enter number of password you need: ")) # USER INPUT NUMBER OF PASSWORD

for i in range(n):# PASSWORD WILL GENERATE UPTO N NUMBER
    password="".join(random.sample(passw,l)) #THE JOIN() JOINS RANDOM ALPHABETS, NUMBERS AND SPECIAL CHARACTERS UPTO USER SPECIFIED LENGTH
    print(password)

