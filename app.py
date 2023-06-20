import numpy as np
from lar import Database, MIN_SEARCH_RADIUS, MAX_SEARCH_RADIUS
from lar.utils import prune_str_list, add_to_loc, to_db_names
from flask import Flask, jsonify
from urllib.parse import unquote

## Author(s): Josue N Rivera

app = Flask(__name__)
dt = Database(host = "mongodb://localhost:27017/")

@app.route('/')
def index():
    return jsonify("It works!")

@app.route('/test/<lat>', methods=['GET'])
def test(lat:str):
    lat = float(lat)
    return jsonify("It works! " + str(lat) + " " + str(type(lat) == float))

@app.route('/adds/<adds>/<dbs>', methods=['GET'])
def adds(adds: str, dbs: str):

    lat, lon, radius = add_to_loc(str(unquote(adds)))
    radius = np.clip(radius, MIN_SEARCH_RADIUS, MAX_SEARCH_RADIUS)

    collections = to_db_names([int(i) for i in unquote(dbs).split(",")])
    collections = prune_str_list(collections)
    collections = ["Hospitals"] if not len(collections) else sorted(collections)
    
    results = {}
    
    for col in collections:
        results[col] = dt.search(col, (lat, lon, radius))

    return jsonify(results)

@app.route('/locs/<lat>,<lon>,<radius>/<dbs>', methods=['GET'])
def locs(lat: str, lon: str, radius: str, dbs: str):

    lat, lon, radius = (float(unquote(lat)), float(unquote(lon)), float(unquote(radius)))
    radius = np.clip(radius, MIN_SEARCH_RADIUS, MAX_SEARCH_RADIUS)

    collections = to_db_names([int(i) for i in unquote(dbs).split(",")])
    collections = prune_str_list(collections)
    collections = ["Hospitals"] if not len(collections) else sorted(collections)
    
    results = {}
    
    for col in collections:
        results[col] = dt.search(col, (lat, lon, radius))

    return jsonify(results)

if __name__ == '__main__':
    app.run()
