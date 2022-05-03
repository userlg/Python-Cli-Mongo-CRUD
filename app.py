from unittest import skip
from urllib.parse import _ResultMixinStr
from colorama import init, Fore
from dotenv import find_dotenv, load_dotenv
from pprint import pprint as pp
from pymongo import MongoClient, errors
from os import environ
import datetime
import socket

# <--------Colors---------->
green = Fore.GREEN
white = Fore.WHITE
red = Fore.RED
yellow = Fore.YELLOW
blue = Fore.BLUE
cyan = Fore.CYAN
MONGODB_HOST = socket.gethostbyname(socket.gethostname())


def input_data(context: str) -> str:
    i = 0
    while(i == 0):
        res = input(yellow + f'Type the post {context} \n\t' + white)
        i = len(res)

    return res

# Structure Documents Post


post = {
    "title": "",
    "description": "",
    "created_at": "",
}


def start_connection() -> MongoClient:
    load_dotenv(find_dotenv())

    try:
        mongo = MongoClient(environ.get(
            'MONGODB_URL'), serverSelectionTimeoutMS=environ.get('MONGODB_TIMEOUT'))
        print('OK -- Connected to MongoDB at server %s' % (MONGODB_HOST))
        return mongo
    except errors.ServerSelectionTimeoutError as e:
        print(e)
        return None
    except errors.ConnectionFailure as e:
        print(e)
        return None


# This method allow insert a post in the database
def insert_post(db):
    collection = db.posts
    document = post
    document['title'] = input_data('title')
    document['description'] = input_data('description')
    document['created_at'] = datetime.datetime.now()

    try:
        document_id = collection.insert_one(document).inserted_id
        print(yellow + '\n\tId Object Inserted--->' +
              str(document_id) + '\n\n' + white)
    except errors.CollectionInvalid as e:
        print(e)


def get_all_post(db) -> None:
    collection = db.posts
    results = collection.find()
    #Count the documents inside the collection
    documents = collection.count_documents({})
    if  documents == 0:
        print(yellow + "\n\n\t\t No posts registered \n\n" + white)
    else:
       for result in results:
         pp(result, indent=10, width=200)


# This method works to find an specific post by its title
def find_post(title: str, db) -> None:
    collection = db.posts
    result = collection.find_one({"title": title})
    if result:
        pp(result)
    else:
        print(red + '\n\t Post not found \n\n' + white)


# This method allows find an post and deleted

def main() -> None:

    mongo_conection = start_connection()
    if mongo_conection:
        db = mongo_conection.Post
        #pp(mongo_conection.list_database_names(), indent=5, width=160)
        # insert_post(mongo_conection.Post)
        get_all_post(db)
        # find_post('test',db)
    else:
        print(red + '\n\t\t  Database Conection Failed --> Mongo Message \n\n' + white)


if __name__ == '__main__':
    main()

    '''
    For This Project you Need Mongodb services Installed and running. Also you need A database called Post and one collection
    called posts in plural
    '''
