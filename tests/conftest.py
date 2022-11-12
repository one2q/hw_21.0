import pytest

from first_attempt import Storage


@pytest.fixture(autouse=True)
def item_in():
	res = {
		'tea':1
	}
	return res