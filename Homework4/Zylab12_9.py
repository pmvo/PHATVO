#Name: Phat Vo
#PSID: 2024127
#Zylab 12.9

if __name__=='__main__':
    list= []
    while True:
        user_input = input()
        txt_split = user_input.split()
        if txt_split[0]=='-1':
            break
        else:
            try:
                if isinstance(int(txt_split[1]),int):
                    print(txt_split[0], int(txt_split[1])+1)
                else:
                    raise ValueError()

            except ValueError as expt:
                print(txt_split[0],"0")

