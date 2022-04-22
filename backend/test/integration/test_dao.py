import pytest
import unittest.mock as mock

from src.util.dao import DAO

@pytest.fixture
def sut():
    mockedDao = mock.MagicMock()
    