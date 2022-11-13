import pytest



@pytest.fixture(autouse=True)
def item_in():
	res = {
		'tea': 1
	}
	return res