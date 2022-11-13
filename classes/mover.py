from classes.base import StorageBase
from classes.request import Request
from custom_exceptions import SpaceException


class Mover:
	"""
	Класс курьер который "переносит" вещи между хранилищами
	"""
	def __init__(self, request: Request, storages: dict[str | StorageBase]):
		self._request = request
		self._from_place = storages.get(self._request.from_place)
		self._to_place = storages.get(self._request.to_place)

	def move(self):
		print('Проверяем есть ли место в пункте назначения')
		if self._request.amount <= self._to_place.get_free_space():
			print('Место есть, забираю товар')
			self._from_place.remove(self._request.name, self._request.amount)
			print('Доставляю товар')
			self._to_place.add_items(self._request.name, self._request.amount)
			print('Товар доставлен, всего хорошего!')
		else:
			raise SpaceException

