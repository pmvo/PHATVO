#Name: Phat Vo
#PSID: 2024127
print("Birthday Calculator")
print("Current day")
current_month = int(input("Month: "))
current_day = int(input("Day: "))
current_yr = int(input("Year: "))
print("Birthday")
birth_month = int(input("Month: "))
birth_day = int(input("Day: "))
birth_yr = int(input("Year: "))

if birth_yr > current_yr or birth_yr < 0 or current_yr < 0 or 31<current_day<0 or 31<birth_day<0 or 12<current_month<0 or 12<birth_month<0: #Check if the input is correct: current year has to > birth year, day must be from 1 to 31 and month must be from 1 to 12
    print("Invalid input!")
else:
    if current_month > birth_month or (current_month == birth_month and current_day >= birth_day) : #Check if it passes the birthday
        age = current_yr - birth_yr
        print("You are ", age, " years old")
        if birth_month == current_month and birth_day == current_day: #Check for the birthday
            print("Happy Birthday!")
    else:
        age = current_yr - birth_yr - 1
        print("You are ", age, " years old")


