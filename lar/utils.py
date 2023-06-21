from typing import List, Tuple
import osmnx as ox
from pyproj import Geod
import requests

## Author(s): Josue N Rivera, Richard D

def prune_str(text: str) -> str:
    return  text.replace("_", "").replace(" ", "").upper()

def prune_str_list(texts: List[str]) -> List[str]:
    return [prune_str(text) for text in texts]

def to_db_names(db_codes: List[int], db_map:dict) -> List[str]:
    return prune_str_list([db_map[i] for i in db_codes])

def add_to_loc(adds: str) -> Tuple[float]:

    polygon = ox.geocode_to_gdf(adds, buffer_dist=1000)
    area = polygon.geometry.iloc[0]

    point = area.centroid
    rectangle = area.minimum_rotated_rectangle

    corner = rectangle.exterior.coords[0]
    _, __, radius = Geod(ellps=polygon.crs.name.replace(" ", "")).inv(point.x, point.y, corner[0], corner[1])

    return (point.x, point.y, radius)

def download_dataset(save_path:str, db_url_id: str) -> None:

    response= requests.get(f"https://opendata.arcgis.com/api/v3/datasets/{db_url_id}"+
                           "/downloads/data?format=geojson&spatialRefId=4326&where=1%3D1")

    with open(save_path, "wb") as f:
        f.write(response.content)
