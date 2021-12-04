#Name: Phat Vo
#PSID: 2024127
#Final Project Part 2
import csv
from datetime import date,datetime

class Inventory:
    def __init__(self):
        self.brand = ''
        self.type = ''
        self.status = ''
        self.price = 0.00
        self.servicedate = ''


if __name__=="__main__":
    # Read the ManufacturerList.csv file, and create a dictionary ,named dict, using ID as the key and brand name, type, and status (damaged or not) as values
    dict = {}
    with open('ManufacturerList.csv', 'r') as file:
        ml_list = csv.reader(file, delimiter=',')
        for row in ml_list:
            key = row[0]
            dict[key] = Inventory()
            dict[key].brand = row[1].strip()
            dict[key].type = row[2].strip()
            dict[key].status = row[3].strip()

    # Read the PriceList.csv file, add to the dictionary using ID as the key and price as the value
    with open('PriceList.csv', 'r') as file:
        price_list = csv.reader(file, delimiter=',')
        for row in price_list:
            key = row[0]
            dict[key].price = row[1].strip()

    # Read the ServiceDatesList.csv file, add to the dictionary using ID as the key and service date as the value
    with open('ServiceDatesList.csv', 'r') as file:
        sd_list = csv.reader(file, delimiter=',')
        for row in sd_list:
            key = row[0]
            if key in dict:
                dict[key].servicedate = row[1].strip()

    while True:
        # Read the user input, allow 'q' to quit
        userinput = input("What are you looking for ('q' to quit the program):\n")
        if userinput.lower()=="q" or userinput.lower()=="quit":
            break
        else:
            list_input = userinput.split()
            for i in range(len(list_input)):
                list_input[i] = list_input[i].lower()


            # Get a current date from the system with the format of dd/mm/yyyy
            today = date.today()
            currentdate = today.strftime('%m/%d/%Y')
            currentdate = datetime.strptime(currentdate, '%m/%d/%Y')

            #Create a list to contain all the item type and item manufacturer
            list_type = []
            list_brand = []
            for key in dict:
                if dict[key].type.lower() not in list_type:
                    list_type.append(dict[key].type.lower())
                if dict[key].brand.lower() not in list_brand:
                    list_brand.append(dict[key].brand.lower())

            count_type = 0
            for x in list_type:
                if x in list_input:
                    types = x
                    count_type += 1
            count_brand = 0
            for y in list_brand:
                if y in list_input:
                    brands = y
                    count_brand += 1
            suggest = ["", "", "", 0] #create the suggest list to store the best matched item
            if count_brand > 1 or count_type > 1 or count_type == 0 or count_brand == 0:
                print("No such item in inventory\n") #Print a message(“No such item in inventory”) if either the manufacturer or the item type are not in the inventory, more that one of either type is submitted or the combination is not in the inventory
            else:
                for key in dict:
                    service_date = datetime.strptime(dict[key].servicedate, '%m/%d/%Y')
                    #Store the item that matches the user input, has no damaged status, has no expired service date , and has the highest price in the suggest list
                    if dict[key].type == types and dict[key].brand.lower() == brands and dict[key].status != 'damaged' and (currentdate > service_date) == False:
                        if (float(suggest[3]) < float(dict[key].price)):
                            suggest[0] = key
                            suggest[1] = dict[key].brand
                            suggest[2] = dict[key].type
                            suggest[3] = float(dict[key].price)
                if (suggest[0] != ""):
                    #Print out the suggested item including: item ID, Manufacturer name, item type and price
                    print("Your item is:")
                    print("{:<12} {:<20} {:<12} {:<12}".format('Item ID', 'Manufacturer Name', 'Item Type', 'Price'))
                    print("{:<12} {:<20} {:<12} {:<12}".format(suggest[0], suggest[1], suggest[2], str(suggest[3])))
                else:
                    print("No such item in inventory\n")
                #Create a consider dictionary with the key is the item ID and the value is the absolute value of the difference between item price and suggested item price
                consider = {}
                for key in dict:
                    service_date = datetime.strptime(dict[key].servicedate, '%m/%d/%Y')
                    if dict[key].type == types and dict[key].brand.lower() != brands and dict[key].status != 'damaged'and (currentdate > service_date) != True :
                        consider[key] = abs(int(dict[key].price) - suggest[3])

                #Print information about the same item type from another manufacturer that closes in price to the output item
                if len(consider)!=0:
                    closest_item = str(min(consider, key=consider.get))
                    print("\nYou may, also, consider:")
                    print("{:<12} {:<20} {:<12} {:<12}".format('Item ID', 'Manufacture Name', 'Item Type', 'Price'))
                    print("{:<12} {:<20} {:<12} {:<12}\n".format(closest_item, dict[closest_item].brand,dict[closest_item].type, dict[closest_item].price))
                else:
                    print("\nYou currently have the best item")
                    print("The other items are either damaged or out of service date\n")




