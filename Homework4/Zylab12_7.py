#Name: Phat Vo
#PSID: 2024127
#Zylab 12.7
def get_age():
    user_age = int(input())
    if user_age < 18 or user_age > 75:
        raise ValueError('Invalid age.')
    return(user_age)
def fat_burning_heart_rate(age):
    return 0.7 * (220-age)

if __name__=='__main__':
    try:
        age=get_age()
        fat_burn=fat_burning_heart_rate(age)
        print('Fat burning heart rate for a {} year-old: {} bpm'.format(age,fat_burn))

    except ValueError as excpt:
        print(excpt)
        print('Could not calculate heart rate info.\n')