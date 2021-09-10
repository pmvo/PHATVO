# Name: Phat Vo
# PSID: 2024127
import math
areaby1gallon = 350
#Part 1
height = int(input("Enter wall height (feet):\n"))
width = int(input("Enter wall width (feet):\n"))
area = width * height
print("Wall area:",area,"square feet")

#Part 2
gallon_need = area / areaby1gallon
print("Paint needed:",'{:.2f}'.format(gallon_need),"gallons")

#Part 3
can_need = math.ceil(gallon_need)
print("Cans needed:",can_need,"can(s)")

#Part 4
color = {
    'red': 35,
    'blue': 25,
    'green': 23
}
user_color = input("\nChoose a color to paint the wall:\n")
cost = color[user_color] * can_need
print("Cost of purchasing",user_color,"paint: ${}".format(cost))