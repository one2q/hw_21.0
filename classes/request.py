from classes.base import StorageBase

from classes.shop_and_store import Shop, Store
from custom_exceptions import RequestException, RequestStorageException


class Request:
	def __init__(self, string: str):
		result = string.lower().split(' ')

		if len(result) != 7:
			raise RequestException

		if result[4] not in ('склад', 'магазин'):
			raise RequestStorageException

		if result[6] not in ('склад', 'магазин'):
			raise RequestStorageException

		self.name = result[2]
		self.amount = int(result[1])
		self.from_place = result[4]
		self.to_place = result[6]


######################################
#
# fruits = {
# 	'apple': 5,
# 	'orange': 3,
# 	'watermelon': 2,
# }
# vegetables = {
# 	'tomato': 5,
# 	'carrot': 7,
# }
#
# shop = Shop(fruits)
# store = Store(vegetables)
#
# storages = {
# 	'магазин': shop,
# 	'склад': store,
# }


# a = Request('Доставить 3 собачки из склад в магазин')
#
# print(a.amount)
# print()
# # print(a.storages['магазин'].get_items())
# print()
# print(a.name)
# print(a.from_place)
# print(a.to_place)


