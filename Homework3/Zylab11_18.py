#Name: Phat Vo
#PSID: 2024127
#Zylab 11.18

list=[]
list = input().split()
for i in range(len(list)):
    list[i]=int(list[i])
list.sort()
for i in range(len(list)):
    if list[i]>=0:
        print(list[i],end=' ')
