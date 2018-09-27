#!/usr/bin/python3

###### this is the first .py file ###########

####### write your code here ##########

# ps1.py is to check the valid crosses
def find_pattern(list1 , i, j):
    countr = list()
    # keeping i and j stored in another variables to recover them afterwards.
    a=i
    b=j
    # initialising counters for differentdirections

    count1=0
    count2=0
    count3=0
    count4=0
    count=0

    #print(list1)
    #print(i)
    #print(j)
    #tracing around the given element in a list.
    if list1[i][j]=='S':
        count=1
        while (j<(m-1)):
            j=j+1
            if list1[i][j]=='S':
                count1=count1+1
            else:
                break
        i=a
        j=b

        while j>0:
            j=j-1
            if list1[i][j] == 'S':
                count2 = count2+1
            else:
                break
        i=a
        j=b
        while i<(n-1):
            i=i+1
            if list1[i][j] == 'S':
                count3 = count3 +1
            else:
                break
        i=a
        j=b
        while i>0:
            i=i-1
            if list1[i][j] == 'S':
                count4 = count4+1
            else:
                break
        i=a
        j=b


    else:
        count=0
    countr = [count1,count2,count3,count4] # list of all the four counters.
    min_count=min(countr)
    count = (min_count*4)+1
    return count
print("Enter m and n")
n1,n2=input().split(" ")
n=int(n1)
m=int(n2)
list1=[]
count_array = ""
# Input a Array of S and D from user adn store it in list1
for index in range(n):
    s=list(input())
    list1+=[s]

for i in range(n):
    for j in range(m):
        #print(i,j)
        count = find_pattern(list1, i, j)
        count_array=count_array + str(count)
#print(count_array)
final_count = list(count_array)
max1=max(final_count)
final_count.remove(max(final_count))
max2=max(final_count)
print("Output")
print(max1,max2)
