from colorama import init, Fore
from dotenv import find_dotenv, load_dotenv
from pprint import pprint as pp
from pymongo import MongoClient, errors
from os import environ
import datetime

#<--------Colors---------->
green = Fore.GREEN
white = Fore.WHITE
red = Fore.RED
yellow = Fore.YELLOW
blue = Fore.BLUE
cyan = Fore.CYAN

def start_connection() -> MongoClient:
     load_dotenv(find_dotenv())
     
     try:
        mongo =  MongoClient(environ.get('MONGODB_URL'))
        return mongo
     except errors.OperationFailure as e:
         print(e)
         return None



def insert_post(db):
    collection = db.Post
    document = {
        "name":"megas",
        "type": "developer"
    }
    print(collection)
    document_id = collection.insert_one(document).inserted_id
    #print(document_id)
    


def main() -> None:
    #   THis is a Model to a post
    post = {"author": "",
        "text": "",
        "tags": [],
        "date": datetime.datetime.utcnow()}
    init()
    db = start_connection()
    if db:
       pp(db.list_database_names(), indent=5, width=160)
       insert_post(db)
    else:
        print(red + '\n\t\t  Database Conection Failed --> Mongo Message \n\n' + white)




if __name__ == '__main__':
    main()