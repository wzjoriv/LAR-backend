from typing import List, Optional, Union
import pymongo as mg
from pymongo.database import Database as mongo_Database
import json, os
from .utils import prune_str

## Author(s): Josue N Rivera

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

                collection = database[prune_str(fl_dt["name"])]

                for loc in fl_dt["features"]:
                    loc.pop("type")

                    if loc["properties"]["CITY"] != None:
                        loc["properties"]["CITY"] = loc["properties"]["CITY"].upper() 

                collection.insert_many(fl_dt["features"])
                collection.create_index([("properties.CITY", mg.TEXT)])
                collection.create_index([("geometry", mg.GEOSPHERE)])

        return database
    
    def get_collections(self):

        return self.database.collection_names()

    def search(self, collection:str, key:Union[str, tuple]) -> List[dict]:
        """
        returns: 
            - list of geometry dict

        keys options:
            - City

                Example: "City::Dallas"
            - (Latitude, Longitude, Radius in meters)

                Example: (-70.98471383, 41.672747140, 10000)

        Example:
            search("Hospitals", "City::Dallas")
        """
        collection = prune_str(collection)
        key = prune_str(key) if type(key) == str else key

        query = self._filter_key(key)
        return list(self.database[collection].find(query, {"_id": False, "geometry":True}))

    def _filter_key(self, key:Union[str, tuple]) -> dict:

        out = {}

        if type(key) == str:
            keys = key.upper().split("::")
            out = {"properties."+keys[0]: keys[1]}
        elif type(key) == tuple:
            out = {"geometry": {"$near": { "$geometry": 
                                          {"type": 'Point', "coordinates": [key[0], key[1]]}, "$maxDistance": key[2]}}}

        return out

    def __del__(self) -> None:
        self.client.close()

if __name__ == "__main__":
    dt = Database(host = "mongodb://localhost:27017/", data_path = "lar/data/")
    dt.search("Hospitals", "City::Lafayette")
    del dt