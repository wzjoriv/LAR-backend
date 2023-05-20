from typing import List, Optional
import pymongo as mg
from pymongo.database import Database as mongo_Database
import json, os

## Author: Josue N Rivera

class Database():

    def __init__(self, host:str = "mongodb://localhost:27017/", data_path:Optional[str] = None) -> None:
        self.host = host
        self.client = mg.MongoClient(self.host)

        if type(data_path) != type(None) and "LAR" not in self.client.list_database_names():
            self.database = self._setup_mongodb(data_path)
        else:
            self.database = self.client["LAR"]

    def _setup_mongodb(self, data_path:str = "lar/data/") -> mongo_Database:

        database = self.client["LAR"]
        for filename in os.listdir(data_path):
            if filename.endswith('.geojson'):
                with open(os.path.join(data_path, filename), encoding='utf-8') as json_file:
                    fl_dt = json.load(json_file)

                collection = database[fl_dt["name"].upper()]

                locs = fl_dt["features"]
                for loc in locs:
                    loc.pop("type")
                collection.insert_many(fl_dt["features"])

        return database

    def search(self, collection:str, key:str) -> List[dict]:
        """
        returns: 
            - list of geometry dict

        keys:
            - State
            - City
            - Zip
            - Zip4

        Example:
            search("Hospitals", "City::Dallas&&State::TX")
        """
        collection, key = (collection.upper(), key.upper())
        keys = self._key_filter(key)

        pass

    def _key_filter(self, key:str) -> dict:

        return {}

    def __del__(self) -> None:
        self.client.close()


if __name__ == "__main__":
    dt = Database(data_path = "lar/data/")
    ## dt.search("Hospitals", "City::Dallas")
    del dt