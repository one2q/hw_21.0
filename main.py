from classes.mover import Mover
from classes.request import Request
from classes.shop_and_store import Shop, Store
from custom_exceptions import RequestStorageException, RequestException, SrorageExeptions

fruits = {
	'яблоки': 5,
	'апельсины': 3,
	'арбузы': 2,
	'бананы': 2,
}
vegetables = {
	'помидоры': 5,
	'морковь': 7,
	'картофель': 4,
}

shop = Shop(fruits)
store = Store(vegetables)

storages = {
	'магазин': shop,
	'склад': store,
}


def main():
	while True:
		for key, value in storages.items():
			print(f'В/На {key}е сейчас\n{value.get_items()}\n')
		print('Здравствуй user, если хочешь воспользоваться нашими услугами')
		print('Введи строку типа: "Доставить 3 собачки из склад в магазин"\n')
		print('Если хочешь остановить программу, введи "стоп" или "stop"\n')
		user_request = input().lower()
		if user_request == "стоп" or user_request == "stop":
			print("Пока")
			break
		try:
			request = Request(user_request)
			mover = Mover(request, storages)
			mover.move()
		except SrorageExeptions as error:
			print(error.message)
		user_request = None


if __name__ == '__main__':
	main()

