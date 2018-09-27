#!/usr/bin/python3
###### this is the second .py file ###########

####### write your code here ##########

key = [1,1,1]
quer_str = input("Enter Encrypted string")
print(quer_str)
alphabets="abcdefghijklmnopqrstuvwxyz_"
alphabets1=alphabets[0:9]
alphabets2=alphabets[9:18]
alphabets3=alphabets[18:27]
key1=""
key2=""
key3=""
for i in quer_str :
    for j in alphabets1:
        if i==j :
            key1 = key1 + str(i)

    for k in alphabets2:
        if i==k :
            key2 = key2 + str(i)

    for l in alphabets3:
        if i==l:
            key3 = key3 + str(i)
print(key2)
