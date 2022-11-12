from abc import ABC

from classes.abstract import AbstractStorage
from custom_exceptions import SpaceExceptions, ItemExceptions


class StorageBase(AbstractStorage):
	"""
	Base class of Storage
	"""

	def __init__(self, items: dict[str | int], capacity: int):
		self._items = items
		self._capacity = capacity

	def add_item(self, name: str, amount: int):

		if self._items.get(name):
			self._items[name] += amount
			self._capacity -= amount
		else:
			self._items[name] = amount
			self._capacity -= amount

	def remove(self, name: str, amount: int):
		if not self._items.get(name):
			raise ItemExceptions
		if amount == self._items.get(name):
			self._capacity += amount
			self._items.pop(name)
		else:
			self._capacity += amount
			self._items[name] -= amount

	def get_free_space(self) -> int:
		return self._capacity

	def get_items(self) -> str:
		return '\n'.join([f'{key} - {value}' for key, value in self._items.items()])

	def get_unique_items_count(self) -> int:
		return len(self._items)
