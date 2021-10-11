#Name: Phat Vo
#PSID: 2024127

def compare(inputMonth,inputDay,inputYear): #This function is used to generate current system date, and compares it with the user input date
    from datetime import date
    today = date.today()
    currentDay = today.day
    currentMonth = today.month
    currentYear = today.year
#If the user input date is later than current date, return value 0 (Ignore). Or else return value 1
    if currentYear < inputYear:
        return 0
    elif currentYear==inputYear and currentMonth<inputMonth:
        return 0
    elif currentYear==inputYear and currentMonth==inputMonth and currentDay<inputDay:
        return 0
    else:
        return 1


def convert_month(month): #This function is used to convert the month name into the month number
    month_list = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12 } #A dictionary to store the month name and the month number
    if month in month_list:
        return month_list[month]
    else:
        return -1



inputFile = open("inputDates.txt")
for line in inputFile:
    if (line!='-1'):

        split_str = line.split(" ")


        if len(split_str)>=3:
            str_month=split_str[0]
            str_day=split_str[1]
            str_year=split_str[2]

            if convert_month(str_month)!=-1:

                if str_day[-1] ==',':
                    int_day = int(str_day[:len(str_day) - 1])

                    if  int_day<=31:
                        int_month = (convert_month(str_month))

                        if compare(int_month,int_day,int(str_year))==1:
                            print(str(int_month)+'/'+str_day[:len(str_day) - 1]+'/'+str_year)

inputFile.close()


