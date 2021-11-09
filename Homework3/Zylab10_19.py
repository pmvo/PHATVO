#Name: Phat Vo
#PSID: 2024127
#Lab 10.19

class ItemToPurchase:
    def __init__(self,item_name='none',item_price=0,item_quantity=0,item_description='none'):
        self.item_name=item_name
        self.item_price=item_price
        self.item_quantity=item_quantity
        self.item_description=item_description
    def print_item_cost(self):
        print('{} {} @ ${} = ${}'.format(self.item_name,self.item_quantity,int(self.item_price),int(self.item_price*self.item_quantity)))
    def print_item_description(self):
        print('{}: {}'.format(self.item_name,self.item_description))


class ShoppingCart():
    def __init__(self,customer_name='none',current_date='January 1, 2016',cart_items=[]):
        self.customer_name=customer_name
        self.current_date=current_date
        self.cart_items= cart_items

    def add_item(self,itemPurchase):
        self.cart_items.append(itemPurchase)

    def remove_item(self,ItemToRemove):
        flag=0
        for item in self.cart_items:
            if item.item_name==ItemToRemove:
                self.cart_items.remove(item)
                flag=1
                break
        if flag==0:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self,itemPurchase):
        flag=0
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == itemPurchase.item_name:
                flag=1
                if(itemPurchase.item_price==0 and itemPurchase.item_quantity==0 and itemPurchase.item_description=='none'):
                    break
                else:
                    if itemPurchase.item_price!=0:
                        self.cart_items[i].item_price=itemPurchase.item_price
                    if itemPurchase.item_quantity != 0:
                        self.cart_items[i].item_quantity = itemPurchase.item_quantity
                    if itemPurchase.item_description != 'none':
                        self.cart_items[i].item_description = itemPurchase.item_description
                    break
        if flag==0:
                print("Item not found in cart. Nothing modified.")


    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total=0
        for item in self.cart_items:
            total+=(item.item_quantity*item.item_price)
        return total

    def print_total(self):
        total=self.get_cost_of_cart()
        if total==0:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("Number of Items: 0")
            print("\nSHOPPING CART IS EMPTY")
            print("\nTotal: $0")
        else:
            print("{}'s Shopping Cart - {}".format(self.customer_name,self.current_date))
            print("Number of Items:",self.get_num_items_in_cart())
            print()
            for item in self.cart_items:
                item.print_item_cost()
            print("\nTotal: ${}".format(total))

    def print_descriptions(self):
        if len(self.cart_items)==0:
            print("SHOPPING CART IS EMPTY")
        else:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("\nItem Descriptions")
            for item in self.cart_items:
                item.print_item_description()

def print_menu(newCart):
    cart = newCart
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        key = input("\nChoose an option:")
        print()
        while key!='a' and key!='r' and key!='c' and key!='i' and key!='o' and key!='q':
            key = input("Choose an option:\n")
        if key == 'a':
            print("\nADD ITEM TO CART")
            item_name=input("Enter the item name:\n")
            item_description = input('Enter the item description:\n')
            item_price = int(input('Enter the item price:\n'))
            item_quantity = int(input('Enter the item quantity:\n'))
            itemPurchase=ItemToPurchase(item_name,item_price,item_quantity,item_description)
            cart.add_item(itemPurchase)
        elif key == 'r':
            print("REMOVE ITEM FROM CART")
            itemRemove = input("Enter name of item to remove:\n")
            cart.remove_item(itemRemove)
        elif key == 'c':
            print("CHANGE ITEM QUANTITY")
            itemChange = input("Enter the item name:\n")
            quantityChange = int(input("Enter the new quantity:\n"))
            itemPurchase=ItemToPurchase(itemChange,0,quantityChange)
            cart.modify_item(itemPurchase)
        elif key == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif key == 'o':
            print("OUTPUT SHOPPING CART")
            cart.print_total()

        elif key == 'q':
            break

if __name__=='__main__':
    customer_name=input("Enter customer's name:\n")
    current_date=input("Enter today's date:\n")
    print("\nCustomer name:",customer_name)
    print("Today's date:",current_date)
    newCart=ShoppingCart(customer_name,current_date)
    print_menu(newCart)








