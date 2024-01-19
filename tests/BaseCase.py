import unittest
from app import app

class BaseCase(unittest.TestCase):
    def setUp(self):
        # this statement will be executed before testing
        self.app = app.test_client()
        print("Hola chica")
        # self.db = db.get_db() # get db by example
        
    def tearDown(self):
        # this statement will be executed after testing
        # Delete Database collections after the test is complete
        # for collection in self.db.list_collection_names()
        # self.db.drop_collection(collection)
        print("Chica Hola")
        pass