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



userinput=input("What are you looking for:")
list_input=userinput.split()
for i in list_input:
    i=i.lower()

#Get a current date from the system with the format of dd/mm/yyyy
today=date.today()
currentdate = today.strftime('%m/%d/%Y')
currentdate = datetime.strptime(currentdate,'%m/%d/%Y')

list_type=[]
list_brand=[]
for key in dict:
    if dict[key].type.lower() not in list_type:
        list_type.append(dict[key].type.lower())
    if dict[key].brand.lower() not in list_brand:
        list_brand.append(dict[key].brand.lower())
count_type=0
for x in list_type:
    if x in list_input:
        types=x
        count_type += 1

count_brand=0
for y in list_brand:
    if y in list_input:
        brands=y
        count_brand += 1


suggest=["","","",0]
if count_brand>1 or count_type>1 or count_type==0 or count_brand==0:
    print("No such item in inventory")
else:
    for key in dict:
        service_date = datetime.strptime(dict[key].servicedate, '%m/%d/%Y')
        if dict[key].type == types and dict[key].brand.lower()==brands and dict[key].status != 'damaged' and (currentdate>service_date)==False:
            if(suggest[3]<float(dict[key].price)):
                suggest[0]=key
                suggest[1]=dict[key].brand
                suggest[2]=dict[key].type
                suggest[3]=float(dict[key].price)
    print("Your item is:",suggest[0],suggest[1],suggest[2],str(suggest[3]))

    consider = []
    for key in dict:
        service_date = datetime.strptime(dict[key].servicedate, '%m/%d/%Y')
        if dict[key].type == types and dict[key].brand.lower() != brands and dict[key].status != 'damaged' and (currentdate > service_date) == False:
            print("You may also consider", key)


