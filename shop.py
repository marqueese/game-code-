items = {'ammo': 10, 'medkit': 20, 'scam': 30}
def display_items():
     for item, price in items.items():
        print(f'{item}: ${price}')
def purchase_item(item):
    if item in items:
        price = items[item]
        print(f'you have purchased {item} for ${price}.')
    else:
      print(f'{item} is not available in this shop.')
display_items()
item = input('enter the name of the item you would like to purchase: ')
purchase_item(item)