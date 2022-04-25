import os, pymongo, json
from dotenv import dotenv_values
from src.util.validators import getValidator

def dbSim():
    # load the local mongo URL (something like mongodb://localhost:27017)
    LOCAL_MONGO_URL = dotenv_values('.env').get('MONGO_URL')
    # check out of the environment (which can be overridden by the docker-compose file) also specifies an URL, and use that instead if it exists
    MONGO_URL = os.environ.get('MONGO_URL', LOCAL_MONGO_URL)
    # Collection variable
    collection = {}


    # connect to the MongoDB and select the appropriate database
    #print(f'Connecting to collection {collection_name} on MongoDB at url {MONGO_URL}')
    client = pymongo.MongoClient(MONGO_URL)
    database = client.edutask

    # task collection
    if "mock_task" not in database.list_collection_names():
        validator = getValidator("task")
        database.create_collection("task", validator=validator)
    # todo collection
    elif "mock_todo" not in database.list_collection_names():
        validator = getValidator("todo")
        database.create_collection("todo", validator=validator)
    # user collection
    elif "mock_user" not in database.list_collection_names():
        validator = getValidator("user")
        database.create_collection("user", validator=validator)
    # video collection
    elif "mock_video" not in database.list_collection_names():
        validator = getValidator("video")
        database.create_collection("video", validator=validator)
    
    collection = {
        "task": database["task"], 
        "todo": database["todo"],
        "user": database["user"],
        "video": database["video"]
        }

    return collection
