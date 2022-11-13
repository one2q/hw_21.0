from custom_exceptions import RequestException, RequestStorageException


class Request:
	"""
	Класс, который распознает запрос пользователя
	"""
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
