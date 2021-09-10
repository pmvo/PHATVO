# Name: Phat Vo
# PSID: 2024127

#Part 1
lemon_juice1 = float(input("Enter amount of lemon juice (in cups):\n"))
water1 = float(input("Enter amount of water (in cups):\n"))
agave1 = float(input("Enter amount of agave nectar (in cups):\n"))
serving1 = float(input("How many servings does this make?\n"))

print("\nLemonade ingredients - yields",'{:.2f}'.format(serving1),"servings")
print('{:.2f}'.format(lemon_juice1),"cup(s) lemon juice")
print('{:.2f}'.format(water1),"cup(s) water")
print('{:.2f}'.format(agave1),"cup(s) agave nectar\n")

#Part 2
serving2 = float(input("How many servings would you like to make?\n"))
lemon_juice2 = (lemon_juice1 / serving1) * serving2
water2 = (water1 / serving1) * serving2
agave2 = (agave1 / serving1) * serving2
print("\nLemonade ingredients - yields",'{:.2f}'.format(serving2),"servings")
print('{:.2f}'.format(lemon_juice2),"cup(s) lemon juice")
print('{:.2f}'.format(water2),"cup(s) water")
print('{:.2f}'.format(agave2),"cup(s) agave nectar\n")

#Part 3
gallon_lemonjuice = lemon_juice2 / 16
gallon_water = water2 / 16
gallon_agave = agave2 / 16
print("Lemonade ingredients - yields",'{:.2f}'.format(serving2),"servings")
print('{:.2f}'.format(gallon_lemonjuice),"gallon(s) lemon juice")
print('{:.2f}'.format(gallon_water),"gallon(s) water")
print('{:.2f}'.format(gallon_agave),"gallon(s) agave nectar")