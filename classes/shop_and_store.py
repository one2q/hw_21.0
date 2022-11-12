from classes.base import StorageBase
from custom_exceptions import ShopUniqueExceptions


class Store(StorageBase):
	def __init__(self, items: dict[str | int], capacity: int = 100):
		super().__init__(items, capacity)


class Shop(StorageBase):
	def __init__(self, items: dict[str | int], capacity: int = 20):
		super().__init__(items, capacity)

	def add_item(self, name: str, amount: int):
		if self.get_unique_items_count() == 5:
			raise ShopUniqueExceptions
		super().add_item(name, amount)