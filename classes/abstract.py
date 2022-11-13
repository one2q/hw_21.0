from abc import ABC, abstractmethod


class AbstractStorage(ABC):
	"""
	Abstract class of Storage
	"""

	@abstractmethod
	def add_items(self, name: str, amount: int):
		pass

	@abstractmethod
	def remove(self, name: str, amount: int):
		pass

	@abstractmethod
	def get_free_space(self):
		pass

	@abstractmethod
	def get_items(self):
		pass

	@abstractmethod
	def get_unique_items_count(self):
		pass