from typing import List, Tuple
import osmnx as ox
from pyproj import Geod
from shapely import Point
import json

## Author(s): Josue N Rivera

with open("config.json") as f:
    __config = json.load(f)
    _database_name = __config.names

def to_db_names(db_codes: List[int]) -> List[str]:
    return [_database_name[i] for i in db_codes]

def prune_str(text: str) -> str:
    return  text.replace("_", "").replace(" ", "").upper()

def prune_str_list(texts: List[str]) -> List[str]:
    return [prune_str(text) for text in texts]

def add_to_loc(adds: str) -> Tuple[float]:

    polygon = ox.geocode_to_gdf(adds, buffer_dist=1000)
    area = polygon.geometry.iloc[0]

    point = area.centroid
    rectangle = area.minimum_rotated_rectangle

    corner = rectangle.exterior.coords[0]
    _, __, radius = Geod(ellps=polygon.crs.name.replace(" ", "")).inv(point.x, point.y, corner[0], corner[1])

    return (point.x, point.y, radius)
