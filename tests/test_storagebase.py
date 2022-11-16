from classes.base import StorageBase


class TestStorageBase:

	def test_get_items(self, storage):
		assert storage.get_free_space() == 7

	def test_get_unique_items_count(self, storage):
		assert storage.get_unique_items_count() == 1

	def test_add_items(self, storage):
		storage.add_items('carrot', 4)
		assert storage.get_free_space() == 3
		assert storage.get_unique_items_count() == 2
		assert storage._items['carrot'] == 4

	def test_remove(self, storage):
		storage.remove('apple', 2)
		assert storage.get_free_space() == 9
		storage.remove('apple', 1)
		assert storage.get_free_space() == 10
		assert storage.get_unique_items_count() == 0
