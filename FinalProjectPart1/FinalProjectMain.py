#Name: Phat Vo
#PSID: 2024127
import csv
from datetime import date,datetime

class Inventory:
    def __init__(self):
        self.brand = ''
        self.type = ''
        self.status = ''
        self.price = 0.00
        self.servicedate = ''

#Read the ManufacturerList.csv file, and create a dictionary ,named dict, using ID as the key and brand name, type, and status (damaged or not) as values
dict={}
with open('ManufacturerList.csv','r') as file:
    ml_list = csv.reader(file,delimiter=',')
    for row in ml_list:
        key = row[0]
        dict[key] = Inventory()
        dict[key].brand = row[1]
        dict[key].type = row[2]
        dict[key].status = row[3]

#Read the PriceList.csv file, add to the dictionary using ID as the key and price as the value
with open('PriceList.csv','r') as file:
    price_list = csv.reader(file,delimiter=',')
    for row in price_list:
        key = row[0]
        dict[key].price = row[1]

#Read the ServiceDatesList.csv file, add to the dictionary using ID as the key and service date as the value
with open('ServiceDatesList.csv','r') as file:
    sd_list = csv.reader(file,delimiter=',')
    for row in sd_list:
        key=row[0]
        if key in dict:
            dict[key].servicedate=row[1]

#Part a. Create a list to store all the brand name and doesn't contain duplicates, then sort alphabetically
sort_brand_list = []
for key in dict:
    if dict[key].brand not in sort_brand_list:
        sort_brand_list.append(dict[key].brand)
sort_brand_list.sort()

#Create a dictionary, named brand_ID, using brand names as the key, and IDs as values. (If one brand name has more than one IDs, create a list to contain all the IDs)
brand_ID={}
for key in dict:
    if dict[key].brand not in brand_ID:
        brand_ID[dict[key].brand]=list(key.split(" "))
    else:
        brand_ID[dict[key].brand].append(key)

#Create a FullInventory.csv file. Each row contains: item ID, manufacturer name (sorted alphabetically), item type, price, service date, and status if it is damaged
with open('FullInventory.csv','w', newline='') as csvfile:
    write=csv.writer(csvfile)
    for brand in sort_brand_list:
        for value in brand_ID[brand]:
            write.writerow([value,brand,dict[value].type,dict[value].price,dict[value].servicedate,dict[value].status])


#Part b. Create a dictionary, named type ID, using item type as the key, and IDs as values. (If one item type has more than one IDs, create a list to contain all the IDs)
type_ID={}
for key in dict:
    if dict[key].type not in type_ID:
        type_ID[dict[key].type] = list(key.split(" "))
    else:
        type_ID[dict[key].type].append(key)

#Sort the key ID from lowest to largest
for item in type_ID.values():
    item.sort(key=int)

#Create a file(The name contain item type + Inventory.csv(For example: LaptopInventory.csv). Each row contains: item ID, manufacturer name, price, service date, and status if it is damaged. The items should be sorted by their item ID.
for type_key in type_ID.keys():
    with open(type_key.capitalize()+'Inventory.csv','w',newline='') as csvfile:
        write=csv.writer(csvfile)
        for ID_value in type_ID[type_key]:
            write.writerow([ID_value,dict[ID_value].brand, dict[ID_value].price, dict[ID_value].servicedate, dict[ID_value].status])

#Part c. Get a current date from the system with the format of dd/mm/yyyy
today=date.today()
currentdate = today.strftime('%m/%d/%Y')
currentdate = datetime.strptime(currentdate,'%m/%d/%Y')

#Create a PastServiceDateInventory.csv file storing all the items that past the service date. Each row contains: item ID, manufacturer name, item type, price, service date, and status if it is damaged
with open('PastServiceDateInventory.csv','w', newline='') as csvfile:
    write=csv.writer(csvfile)
    for key in dict:
        service_date = datetime.strptime(dict[key].servicedate, '%m/%d/%Y')
        if (currentdate>service_date)==True:
            write.writerow([key,dict[key].brand,dict[key].type,dict[key].price,dict[key].servicedate,dict[key].status])

#Part d. Create a list to store all the price, then sort them from highest to lowest
sort_price_list = []
for key in dict:
    if dict[key].price not in sort_price_list:
        sort_price_list.append(dict[key].price)
sort_price_list.sort(key=int)
sort_price_list.reverse()

#Create a dictionary, named price_ID, using price as the key, and ID as the value (If one price has more than one IDs, create a list to contain all the IDs)
price_ID={}
for key in dict:
    if dict[key].price not in price_ID:
        price_ID[dict[key].price]=list(key.split(" "))
    else:
        price_ID[dict[key].price].append(key)

#Create a DamagedInventory.csv file storing all the items that are damaged. Each row contains: item ID, manufacturer name, item type, price, service date, and status if it is damaged
with open('DamagedInventory.csv','w', newline='') as csvfile:
    write=csv.writer(csvfile)
    for price in sort_price_list:
        for value in price_ID[price]:
            if dict[value].status.lower()=='damaged':
                write.writerow([value,dict[value].brand,dict[value].type,dict[value].price,dict[value].servicedate])