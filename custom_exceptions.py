class SrorageExeptions(Exception):
	message = "Общая ошибка склада"


class SpaceExceptions(SrorageExeptions):
	""""Ошибка отсутствия свободного места"""
	message = 'Ошибка: Нет свободного места'


class ShopUniqueExceptions(SrorageExeptions):
	""""Ошибка ограничения количества уникальных товаров"""
	message = 'Ошибка: Количество уникальных товаров не может быть больше 5'


class ItemExceptions(SrorageExeptions):
	""""Ошибка отсутствия товаров в наличии"""
	message = 'Ошибка: Нет таких предметов'


class ItemAmountExceptions(SrorageExeptions):
	""""Ошибка количества запрашиваемых товаров"""
	message = 'Ошибка: Нет такого количества товаров'
