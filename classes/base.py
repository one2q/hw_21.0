from abc import ABC

from classes.abstract import AbstractStorage
from custom_exceptions import SpaceException, ItemException, ItemAmountException


class StorageBase(AbstractStorage):
	"""
	Base class of Storage
	"""

	def __init__(self, items: dict[str | int], capacity: int):
		self._items = items
		self._capacity = capacity

	def add_items(self, name: str, amount: int) -> None:
		if self.get_free_space() < amount:
			raise SpaceException
		if self._items.get(name):
			self._items[name] += amount
		else:
			self._items[name] = amount

	def remove(self, name: str, amount: int) -> None:
		if not self._items.get(name):
			raise ItemException
		if amount > self._items.get(name):
			raise ItemAmountException
		if amount == self._items.get(name):
			self._items.pop(name)
		else:
			self._items[name] -= amount

	def get_free_space(self) -> int:
		return self._capacity - sum(self._items.values())

	def get_items(self) -> str:
		return '\n'.join([f'{key} - {value}' for key, value in self._items.items()])

	def get_unique_items_count(self) -> int:
		return len(self._items)
