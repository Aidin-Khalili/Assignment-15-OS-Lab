from math import *
arr = []
n = abs(int(input("Please enter size of array : ")))
for i in range(0, n):
    temp = int(input())
    arr.append(temp) 
flag = True
for i in range(0, floor(len(arr)/2)):
        if arr[i] == arr [len(arr)-(i+1)]:
            continue
        else :
            flag = False
            break
if (flag == False):
    print("Not Symmetric")
else:
    print("Symmetric")
