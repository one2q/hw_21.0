import pytest

from classes.base import StorageBase


@pytest.fixture()
def storage():
    yield StorageBase({'apple': 3}, 10)

