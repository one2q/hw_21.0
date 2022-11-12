import pytest

from first_attempt import Storage


class TestStorage:

	def test_get_free_space(self):
		storage = Storage(10)
		assert storage._get_free_space() == 10, "Capacity error"

	def test_check_item_in(self):
		storage = Storage(10)
		storage.add_items('tea', 3)
		assert storage.check_item_in('tea') == True, 'Item_in error'

	def test_check_unique_items_count(self):
		storage = Storage(10)
		storage.add_items('tea', 10)
		assert storage._get_unique_items_count() == 1, 'Unique items error'

