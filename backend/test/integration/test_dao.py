import pytest, pymongo, json
import unittest.mock as mock
from src.util.dao import DAO
from src.util.mockDB import MockDB

@pytest.fixture
def sutTask():
    collection = MockDB.dbSim()
    sut = DAO("task")
    sut.collection = collection['task']
    return sut

@pytest.fixture
def sutTodo():
    collection = MockDB.dbSim()
    sut = DAO("todo")
    sut.collection = collection['todo']
    return sut

def test_task_valid_create1(sutTask):
    data = {
        "title": "Python Assignment",
        "description": "Learn the basics of python."
    }
    res = sutTask.create(data)
    assert res['title'] == data['title']

def test_task_invalid_create1(sutTask):
    data = {
        "title": 69,
        "description": False
    }
    with pytest.raises(pymongo.errors.WriteError):
        sutTask.create(data)
def test_task_valid_create2(sutTask):
    data = {
        "title": "ASM x86 address",
        "description": "Learn how to make calls to various addresss in x86 arch."
    }
    res = sutTask.create(data)
    assert res['title'] == data['title']

def test_task_invalid_create2(sutTask):
    data = {
        "title": "Let's learn Vim",
    }
    with pytest.raises(pymongo.errors.WriteError):
        sutTask.create(data)

def test_todo_valid_create1(sutTodo):
    data = {
        "description": "Create test for get_user_by_email, EduTask"
    }
    res = sutTodo.create(data)
    assert res['description'] == data['description']
