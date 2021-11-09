#Name: Phat Vo
#PSID: 2024127
#Zylab 11.27
my_dict={}
for n in range(1,6):
    key=input("Enter player {}'s jersey number:\n".format(n))
    val=input("Enter player {}'s rating:\n".format(n))
    my_dict[key]=val
    print()
sort_list=[]
for key in my_dict.keys():
    if key not in sort_list:
        sort_list.append(key)
sort_list.sort(key=int)
print("ROSTER")
for x in sort_list:
    print("Jersey number: {}, Rating: {}".format(x,my_dict[x]))

while True:
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit\n")
    user_input=input("Choose an option:\n").lower()
    if user_input=="a":
        new_jersey=input("Enter a new player's jersey number:\n")
        new_rate=input("Enter the player's rating:\n")
        my_dict[new_jersey]=new_rate
    elif user_input=="d":
        delete_jersey=input("Enter a jersey number:\n")
        if delete_jersey in my_dict.keys():
            my_dict.pop(delete_jersey, None)
        print(my_dict)
    elif user_input=="u":
        update_jersey=input("Enter a jersey number:\n")
        update_rate=input("Enter a new rating for player:\n")
        my_dict.update({update_jersey:update_rate})
    elif user_input=="r":
        rate=int(input("Enter a rating:\n"))
        print("\nABOVE",rate)
        new_list=[]
        for x in my_dict:
            if int(my_dict[x])>rate:
                if x not in new_list:
                    new_list.append(x)
                new_list.sort(key=int)
        for value in new_list:
            print("Jersey number: {}, Rating: {}".format(value,my_dict[value]))
    elif user_input=="o":
        for key in my_dict.keys():
            if key not in sort_list:
                sort_list.append(key)
        sort_list.sort(key=int)
        print("ROSTER")
        for x in sort_list:
            if x in my_dict.keys():
                print("Jersey number: {}, Rating: {}".format(x, my_dict[x]))
    elif user_input=="q":
        break


