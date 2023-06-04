import sys
import os
sys.path.append(os.path.abspath('..'))
import lar

## Author: Josue N Rivera
## Requires server to be ruuning first


def test_access_db_with_data_path():
    dt = lar.Database(host = "mongodb://localhost:27017/", data_path = "lar/data/")
    assert "LAR" in dt.client.list_database_names()
    del dt

def test_access_db_without_data_path():
    dt = lar.Database(host = "mongodb://localhost:27017/")
    assert "LAR" in dt.client.list_database_names()
    del dt

def test_query_results_city():
    dt = lar.Database(host = "mongodb://localhost:27017/", data_path = "lar/data/")
    assert len(dt.search("Hospitals", "City::Lafayette")) == 25
    del dt

def test_query_results_lon_lat_rad():
    dt = lar.Database(host = "mongodb://localhost:27017/", data_path = "lar/data/")
    assert len(dt.search("Hospitals", (-70.98471383, 41.672747140, 10000))) == 3
    del dt

def test_all_collections():
    dt = lar.Database(host = "mongodb://localhost:27017/", data_path = "lar/data/")
    assert sorted(["HOSPITALS", "FIRESTATIONS", "PUBLICSCHOOLS", "LOCALLAWENFORCEMENT", "AVIATIONFACILITIES"]) \
            == sorted(dt.database.list_collection_names())
    del dt




