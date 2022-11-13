from classes.base import StorageBase
from custom_exceptions import ShopUniqueException


class Store(StorageBase):
	"""
	Класс склад, вместимость по умолчанию 100
	"""
	def __init__(self, items: dict[str | int], capacity: int = 100):
		super().__init__(items, capacity)


class Shop(StorageBase):
	"""
	Класс магазин, вместимость по умолчанию 20
	"""
	def __init__(self, items: dict[str | int], capacity: int = 20):
		super().__init__(items, capacity)

	def add_items(self, name: str, amount: int):
		if self.get_unique_items_count() == 5:
			raise ShopUniqueException
		super().add_items(name, amount)
