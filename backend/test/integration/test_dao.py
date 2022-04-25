import pytest, pymongo, json
import unittest.mock as mock
from src.util.dao import DAO
from src.util.mockDB import dbSim

class TestDayo:
    @pytest.fixture
    def sutTask(self):
        collection = dbSim()
        sut = DAO(collection_name=collection)
        sut.collection["task"]
        return sut