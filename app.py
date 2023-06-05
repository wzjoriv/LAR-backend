from lar import Database
from lar.utils import prune_str_list
from flask import Flask, jsonify

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

@app.route('/locs/<lat>,<lon>,<radius>/<dbs>', methods=['GET'])
def locs(lat: str, lon: str, radius: str, dbs: str):

    lat, lon, radius = (float(lat), float(lon), float(radius))

    collections = prune_str_list(dbs.split(","))
    collections = ["Hospitals"] if not len(collections) else sorted(collections)
    
    results = {}
    
    for col in collections:
        results[col] = dt.search(col, (lat, lon, radius))

    return jsonify(results)

if __name__ == '__main__':
    app.run()