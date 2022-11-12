class SpaceExceptions(Exception):
	""""Ошибка отсутствия свободного места"""

	def __str__(self):
		return 'Ошибка: Нет свободного места'


class ShopUniqueExceptions(Exception):
	""""Ошибка ограничения количества уникальных товаров"""

	def __str__(self):
		return 'Ошибка: Количество уникальных товаров не может быть больше 5'


class ItemExceptions(Exception):
	""""Ошибка отсутствия товаров в наличии"""

	def __str__(self):
		return 'Ошибка: Нет таких предметов'


class ItemAmountExceptions(Exception):
	""""Ошибка количества запрашиваемых товаров"""

	def __str__(self):
		return 'Ошибка: Нет такого количества товаров'
