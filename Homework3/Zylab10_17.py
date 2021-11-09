#Name: Phat Vo
#PSID: 2024127
#Lab 10.17

class ItemToPurchase:
    def __init__(self):
        self.item_name='none'
        self.item_price=0
        self.item_quantity=0
    def print_item_cost(self):
        print('{} {} @ ${} = ${}'.format(self.item_name,self.item_quantity,int(self.item_price),int(self.item_price*self.item_quantity)))


if __name__=='__main__':
    item1=ItemToPurchase()
    print('Item 1')
    item1.item_name=input('Enter the item name:\n')
    item1.item_price=float(input('Enter the item price:\n'))
    item1.item_quantity=int(input('Enter the item quantity:\n'))

    item2 = ItemToPurchase()
    print('\nItem 2')
    item2.item_name = input('Enter the item name:\n')
    item2.item_price = float(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))
    print('\nTOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    print('\nTotal: ${}'.format(int(item1.item_price*item1.item_quantity + item2.item_price*item2.item_quantity)))



