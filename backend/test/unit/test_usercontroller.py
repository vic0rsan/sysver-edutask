import pytest
import unittest.mock as mock

from src.controllers.usercontroller import UserController

@pytest.fixture
def sut(email: str, usersLen: int):
    mockedUserController = mock.MagicMock()
    users = []
    for i in range(usersLen):
        users.append({'email': email})
    mockedUserController.find.return_value = users
    mockedSut = UserController(dao=mockedUserController)
    return mockedSut

@pytest.mark.demo
@pytest.mark.parametrize('email, expected, usersLen', [('jane.doe@gmail.com', {'email': 'jane.doe@gmail.com'}, 1), ('jane.doe@gmail.com', {'email': 'jane.doe@gmail.com'}, 2)])
def test_get_user_by_email(sut, expected):
    '''Test valid email inputs'''
    email = "jane.doe@gmail.com"
    emailRes = sut.get_user_by_email(email)
    assert emailRes == expected

@pytest.mark.demo
@pytest.mark.parametrize('email, usersLen', [('jane.doe.gmail.com', 0)])
def test_invalid_email(sut):
    '''Test invalid email input by changing "@" with "."'''
    email = "jane.doe.gmail.com"
    with pytest.raises(ValueError):
        sut.get_user_by_email(email)

@pytest.mark.demo
@pytest.mark.parametrize('email, expected, usersLen', [('jane.doe@gmail.com', None, 0)])
def test_valid_email_blank_db(sut, expected):
    '''Test valid email with blank db/filter response'''
    email = "tom.doe@gmail.com"
    with pytest.raises(IndexError):
        sut.get_user_by_email(email)