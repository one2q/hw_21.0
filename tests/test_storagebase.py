from classes.base import StorageBase


#TODO Правильно ли создавать экземпляр класса каждый раз?
# Есть ощущение что это можно сделать как то через конфтест\фикстуру
# но я не нашел как((

class TestStorageBase:

	def test_get_items(self):
		tsb = StorageBase({'apple': 3}, 10)
		assert tsb.get_free_space() == 7

	def test_get_unique_items_count(self):
		tsb = StorageBase({'apple': 3}, 10)
		assert tsb.get_unique_items_count() == 1

	def test_add_items(self):
		tsb = StorageBase({'apple': 3}, 10)
		tsb.add_items('carrot', 4)
		assert tsb.get_free_space() == 3
		assert tsb.get_unique_items_count() == 2
		assert tsb._items['carrot'] == 4

	def test_remove(self):
		tsb = StorageBase({'apple': 3}, 10)
		tsb.remove('apple', 2)
		assert tsb.get_free_space() == 9
		tsb.remove('apple', 1)
		assert tsb.get_free_space() == 10
		assert tsb.get_unique_items_count() == 0
