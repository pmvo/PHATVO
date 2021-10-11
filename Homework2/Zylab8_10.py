#Name: Phat Vo
#PSID: 2024127

string1 = str(input())
string_nospace= string1.lower().replace(" ","")
string2= string_nospace[::-1]
if string_nospace==string2:
    print(string1,"is a palindrome")
else:
    print(string1, "is not a palindrome")