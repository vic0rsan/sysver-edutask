import pytest
import unittest.mock as mock

from src.controllers.usercontroller import UserController

def test_valid_email_format():
    mockedDao = mock.MagicMock()
    mockedDao.find.return_value = [{'email': 'jane.doe@gmail.com'}]

    mockedSut = UserController(dao=mockedDao)
    expect = mockedSut.get_user_by_email("jane.doe@gmail.com")

    assert expect == mockedDao.find()[0]

def test_invalid_email_format():
    mockedDao = mock.MagicMock()
    mockedDao.find.return_value = [{}] #Invalid format of emails should not return anything!

    mockedSut = UserController(dao=mockedDao)
    expect = {}
    with pytest.raises(ValueError):
        expect = mockedSut.get_user_by_email("jane.doe.gmail.com")

    assert expect == mockedDao.find()[0]

def test_invalid_empty_email_format():
    mockedDao = mock.MagicMock()
    mockedDao.find.return_value = [{}] #Invalid format of emails should not return anything!

    mockedSut = UserController(dao=mockedDao)
    expect = {}
    with pytest.raises(ValueError):
        expect = mockedSut.get_user_by_email("")

    assert expect == mockedDao.find()[0]

def test_duplicate_emails():
    mockedDao = mock.MagicMock()
    mockedDao.find.return_value = [{'email': 'jane.doe@gmail.com'}, {'email': 'jane.doe@gmail.com'}] #Duplicates should not be allowed!

    mockedSut = UserController(dao=mockedDao)
    expect = mockedSut.get_user_by_email("jane.doe@gmail.com")

    assert expect == mockedDao.find()[0]

def test_valid_email_on_empty_database():
    mockedDao = mock.MagicMock()
    mockedDao.find.return_value = [] #Empty database or email not found

    mockedSut = UserController(dao=mockedDao)
    expect = []
    with pytest.raises(IndexError):
        expect = mockedSut.get_user_by_email("jane.doe@gmail.com")
    assert expect == mockedDao.find()