import pytest

from classes.request import Request
from custom_exceptions import RequestException, RequestStorageException

req = Request('Доставь 4 пирога из склад в магазин')


class TestRequest:

	def test_parsing(self):
		assert req.amount == 4
		assert req.name == 'пирога'
		assert req.from_place == 'склад'
		assert req.to_place == 'магазин'

	def test_request_exception(self):
		with pytest.raises(RequestException):
			Request('Доставь 1 пирога из склад в магазин пожалуйста')

	def test_request_storage_exception(self):
		with pytest.raises(RequestStorageException):
			Request('Доставь 1 пирога из склада в магазин')

	def test_request_s_exception(self):
		with pytest.raises(ValueError):
			Request('Доставь один пирога из склад в магазин')
