import numpy as np
from lar import Database, MIN_SEARCH_RADIUS, MAX_SEARCH_RADIUS
from lar.utils import prune_str, add_to_loc, to_db_names
from flask import Flask, jsonify
from urllib.parse import unquote
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

## Author(s): Josue N Rivera

with open("config.json") as f:
    config = json.load(f)

dt = Database( config=config, host = f"mongodb://{config['host']['mongodb']}:{config['port']['mongodb']}/")

@app.route('/')
def index():
    return jsonify("It works!")

@app.route('/test/<adds>', methods=['GET'])
def test(adds:str):
    
    lon, lat, radius = add_to_loc(str(unquote(adds)))
    radius = np.clip(radius, MIN_SEARCH_RADIUS, MAX_SEARCH_RADIUS)

    return jsonify({"longitude": lon, "latitude": lat, "radius": radius})

@app.route('/adds/<adds>/<dbs>', methods=['GET'])
def adds(adds: str, dbs: str):

    lon, lat, radius = add_to_loc(str(unquote(adds)))
    radius = np.clip(radius, MIN_SEARCH_RADIUS, MAX_SEARCH_RADIUS)

    collections = to_db_names([prune_str(i) for i in unquote(dbs).split(",")], dt.id_to_collection)
    collections = ["Hospitals"] if not len(collections) else sorted(collections)
    
    results = {}
    
    for col in collections:
        results[col] = dt.search(col, (lon, lat, radius))

    return jsonify(results)

@app.route('/locs/<lat>,<lon>,<radius>/<dbs>', methods=['GET'])
def locs(lat: str, lon: str, radius: str, dbs: str):

    lon, lat, radius = (float(unquote(lon)), float(unquote(lat)), float(unquote(radius)))
    radius = np.clip(radius, MIN_SEARCH_RADIUS, MAX_SEARCH_RADIUS)

    collections = to_db_names([prune_str(i) for i in unquote(dbs).split(",")], dt.id_to_collection)
    collections = ["Hospitals"] if not len(collections) else sorted(collections)
    
    results = {}
    
    for col in collections:
        results[col] = dt.search(col, (lon, lat, radius))

    return jsonify(results)

if __name__ == '__main__':
    app.run(host=config['host']['backend'], port=config['port']['backend'])
