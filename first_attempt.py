from abc import ABC, abstractmethod
from dataclasses import dataclass

from custom_exceptions import ShopUniqueExceptions, SpaceExceptions, ItemExceptions, ItemAmountExceptions


class Storage:
	"""Base class for store and shop"""

	def __init__(self, capacity: int):
		self.__items = {}
		self.__capacity = capacity

	def print_items(self) -> str:
		return '\n'.join([f'{key} - {value}' for key, value in self.__items.items()])

	def _get_keys_items(self):
		return [i for i in self.__items.keys()]

	def add_items(self, name: str, amount: int):
		# Check is it enough space
		if amount > self._get_free_space():
			raise SpaceExceptions

		# Shop has restriction for unique items
		if isinstance(self, Shop):
			if self._get_unique_items_count() == 5:
				raise ShopUniqueExceptions

		if self.__items.get(name):
			self.__items[name] += amount
			self.__capacity -= amount
		else:
			self.__items[name] = amount
			self.__capacity -= amount

	def remove(self, name: str, amount: int):

		if not self.check_item_in(name):
			raise ItemExceptions

		if amount > self.__items.get(name):
			raise ItemAmountExceptions

		if amount == self.__items.get(name):
			self.__capacity += amount
			self.__items.pop(name)
		else:
			self.__capacity += amount
			self.__items[name] -= amount

	def check_item_in(self, name: str) -> bool:
		return name in self.__items.keys()

	def _get_free_space(self) -> int:
		return self.__capacity

	def _get_unique_items_count(self) -> int:
		return len(self.__items)


class Shop(Storage):
	def __str__(self):
		return "Магазин"


class Store(Storage):
	def __str__(self):
		return "Склад"


@dataclass
class Request:
	from_place: str
	to: str
	amount: int
	product: str


# a = Shop('shop', 100)
#
# try:
# 	a.add_items('232', 100)
# except SpaceExceptions as e:
# 	print(e)
# except ShopUniqueExceptions as e:
# 	print(e)
#
# v = Request('shop', 'store', 6, 'tea')



