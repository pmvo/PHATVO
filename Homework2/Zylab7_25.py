#Name: Phat Vo
#PSID: 2024127
def exact_change(user_total):
    dollar = user_total//100
    quarter = (user_total%100)//25
    dime = ((user_total%100)%25)//10
    nickel = ((((user_total%100)%25)%10)//5)
    penny = (((user_total%100)%25)%10)%5
    return dollar,quarter,dime,nickel,penny


if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
    if input_val<=0:
        print("no change")
    else:
        if num_dollars>1:
            print("{} dollars".format(num_dollars))
        elif num_dollars==1:
            print("{} dollar".format(num_dollars))
        if num_quarters>1:
            print("{} quarters".format(num_quarters))
        elif num_quarters==1:
            print("{} quarter".format(num_quarters))
        if num_dimes>1:
            print("{} dimes".format(num_dimes))
        elif num_dimes==1:
            print("{} dime".format(num_dimes))
        if num_nickels>1:
            print("{} nickels".format(num_nickels))
        elif num_nickels==1:
            print("{} nickel".format(num_nickels))
        if num_pennies>1:
            print("{} pennies".format(num_pennies))
        elif num_pennies==1:
            print("{} penny".format(num_pennies))
