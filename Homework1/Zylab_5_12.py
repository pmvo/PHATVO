# Name: Phat Vo
# PSID: 2024127

#Part 1
print("Davy's auto shop services\n"+
      "Oil change -- $35\n"+
      "Tire rotation -- $19\n"+
      "Car wash -- $7\n"+
      "Car wax -- $12\n")

#Part 2
user_service1 = input("Select first service:\n")
user_service2 = input("Select second service:\n")

#Part 3+4
service = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12,
    '-': 0
}
total = service[user_service1] + service[user_service2]
print("\nDavy's auto shop invoice\n")

if user_service1 != '-' and user_service2 != '-' :
    print("Service 1: {}, ${}".format(user_service1,service[user_service1]))
    print("Service 2: {}, ${}".format(user_service2,service[user_service2]))
elif user_service1 == '-' and user_service2 != '-':
    print("Service 1: No service")
    print("Service 2: {}, ${}".format(user_service2,service[user_service2]))
elif user_service1 != '-' and user_service2 == '-':
    print("Service 1: {}, ${}".format(user_service1,service[user_service1]))
    print("Service 2: No service")
else:
    print("Service 1: No service")
    print("Service 2: No service")

print("\nTotal: ${}".format(total))