#Name: Phat Vo
#PSID: 2024127

import csv
input_file=str(input())
with open(input_file,"r") as csvfile:
    group = csv.reader(csvfile, delimiter=',')
    dict ={}
    for row in group:
        for item in row:
            if item in dict:
                dict[item]+=1
            else:
                dict[item]=1
    for item in dict:
        print(item, dict[item])