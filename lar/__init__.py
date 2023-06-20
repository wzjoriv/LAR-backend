from .db import Database
import json

## Author: Josue N Rivera

__all__ = ["Database"]

with open("lar/config.json") as f:
    database_name = json.load(f)["db_names"]

MAX_SEARCH_RADIUS = 50000 #meters