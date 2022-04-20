import pytest
import unittest.mock as mock

from src.controllers.usercontroller import UserController

@pytest.fixture
def sut(email: str, usersLen: int):
    mockedUserController = mock.MagicMock()
    users = []
    for i in range(usersLen):
        users.append({'email': email})
    if len(users) == 0:
        users = [None]
    mockedUserController.find.return_value = users
    mockedSut = UserController(dao=mockedUserController)
    return mockedSut

@pytest.mark.demo
@pytest.mark.parametrize('email, expected, usersLen', [('jane.doe@gmail.com', {'email': 'jane.doe@gmail.com'}, 1), ('jane.doe@gmail.com', {'email': 'jane.doe@gmail.com'}, 2), ('jane.doe@gmail.com', None, 0)])
def test_get_user_by_email(sut, expected):
    email = "jane.doe@gmail.com"
    emailRes = sut.get_user_by_email(email)
    assert emailRes == expected

@pytest.mark.demo
@pytest.mark.parametrize('email, usersLen', [('jane.doe.gmail.com', 0)])
def test_invalid_email(sut):
    email = "jane.doe.gmail.com"
    with pytest.raises(ValueError):
        sut.get_user_by_email(email)