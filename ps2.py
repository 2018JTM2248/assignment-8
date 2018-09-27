#!/usr/bin/python3
###### this is the second .py file ###########

####### write your code here ##########
#function definition to rotate a string d elemets to right
def rotate_right(array,d):
    r1=array[0:len(array)-d]  # taking first n-d letters
    r2=array[len(array)-d:]  # last d letters
    rotate = r2+r1   # reversed the order
    return rotate   #return ststement



decrypted=""                        # decrypted string will be stored here
#k1=int(input("Enter the amount by which key1 elemets to be rotated\n Decryption key1 = : "))
#k2=int(input("\nDecryption key2  = : "))
#k3=int(input("\nDecryption key3  = : "))
print("Enter Key")
j1,j2,j3 =input().split(" ")
k1=int(j1)
k2=int(j2)
k3=int(j3)
quer_str = input("Enter Encrypted string\n")
print(quer_str)
alphabets="abcdefghijklmnopqrstuvwxyz_"
alphabets1=alphabets[0:9]
alphabets2=alphabets[9:18]
alphabets3=alphabets[18:27]
# Declaring Strings to store different key characters
key1=""
key2=""
key3=""
# Seperating keys for different range
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

# keys sorted according to input numbers by which they are to be shifted
new_k1=rotate_right(key1,k1)
new_k2=rotate_right(key2,k2)
new_k3=rotate_right(key3,k3)
index1=0
index2=0
index3=0
# Decrypting a string and printing original decrypted string
for i in quer_str:
    for j in new_k1 :
        if i==j:
            decrypted=decrypted+new_k1[index1]
            index1 = index1+1

    for k in new_k2 :
        if i==k :
            decrypted=decrypted+new_k2[index2]
            index2=index2+1

    for l in new_k3 :
        if i==l :
            decrypted=decrypted+new_k3[index3]
            index3=index3+1

print("Decrypted string is : ",decrypted)
