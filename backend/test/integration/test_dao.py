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

@pytest.fixture
def sutUser():
    collection = MockDB.dbSim()
    sut = DAO("user")
    sut.collection = collection['user']
    return sut

@pytest.fixture
def sutVideo():
    collection = MockDB.dbSim()
    sut = DAO("video")
    sut.collection = collection['video']
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

def test_todo_invalid_create1(sutTodo):
    data = {
        "description": None
    }
    with pytest.raises(pymongo.errors.WriteError):
        sutTodo.create(data)
  
def test_user_valid_create1(sutUser):
    data = {
        "firstName": "Jane",
        "lastName": "Doe",
        "email": "jane.doe@gmail.com"
    }
    res = sutUser.create(data)
    assert res['firstName'] == data['firstName']

def test_user_invalid_create1(sutUser):
    data = {
        "firstName": "Tom",
        "lastName": 69,
        "email": "tom.doe$"
    }
    with pytest.raises(pymongo.errors.WriteError):
        sutUser.create(data)

def test_user_invalid_create2(sutUser):
    data = {
        "lastName": "Doe",
        "email": "tom.doe@gmail.com"
    }
    with pytest.raises(pymongo.errors.WriteError):
        sutUser.create(data)

def test_video_valid_create1(sutVideo):
    data = {
        "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    }
    res = sutVideo.create(data)
    assert res['url'] == data['url']

def test_video_invalid_create1(sutVideo):
    data = {
        "url": 1337
    }
    with pytest.raises(pymongo.errors.WriteError):
        sutVideo.create(data)

def test_create_collection_by_include_list(sutUser):
    data = {
        "firstName": "Tom",
        "lastName": "Doe",
        "email": "tom.doe@gmail.com",
        "tasks": []
    }
    sutUser.create(data)

def test_create_duplicate_item():
    data = {
        "firstName": "Jerry",
        "lastName": "Doe",
        "email": "jerry.doe@gmail.com",
        "task": ["test3", "test4", "test3"]
    }
    MockDB.dbCleanUp()