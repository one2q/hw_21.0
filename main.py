from classes import *

# 'store' if from_place == 'shop' else 'shop'

shop = Shop(20)
store = Store(100)

fruits = {
	'apple': 5,
	'orange': 10,
	'watermelon': 7,
}

[store.add_items(name, amount) for name, amount in fruits.items()]
print(store.print_items())
print(shop.print_items())
print('-' * 20)


# request = Request()
answer = True
while answer:
	print(store.print_items())
	print(shop.print_items())
	print('Hi, user')
	product = input('please enter name of product witch u wanna delivery\n').lower()
	amount = int(input('amount\n'))
	from_place = input('from what place u needed to take - shop or store\n').lower()
	to = 'store' if from_place == 'shop' else 'shop'

	request = Request(from_place, to, amount,product)
	print('Thanks, i need time to prepare something')
	if from_place == 'shop':
		if shop.check_item_in(product):
			try:
				shop.remove(product, amount)
				store.add_items(product, amount)
			except ItemExceptions as e:
				print(e)
			except ItemAmountExceptions as e:
				print(e)
		else:
			try:
				raise ItemExceptions
			except ItemExceptions as e:
				print(e)
	else:
		if store.check_item_in(product):
			try:
				store.remove(product, amount)
				shop.add_items(product, amount)
			except ItemExceptions as e:
				print(e)
			except ItemAmountExceptions as e:
				print(e)
		else:
			try:
				raise ItemExceptions
			except ItemExceptions as e:
				print(e)

	print(store.print_items())
	print(shop.print_items())
	break
