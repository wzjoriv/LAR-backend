import requests

dataset_ids={
    "public_schools": "87376bdb0cb3490cbda39935626f6604_0",
    "aviation_facilities": "e6fe35a5120a446a87898c30b6b01bef_0",
    "fire_stations": "0ccaf0c53b794eb8ac3d3de6afdb3286_0",
    "hospitals": "75079bdea94743bcaca7b6e833692639_0",
    "local_law_enforcement_locations": "0d79b978d71b4654bddb6ca0f4b7f830_0"
}

def download_datasets(filename, dataset: str) -> None:
    response= requests.get(f"https://opendata.arcgis.com/api/v3/datasets/{dataset}/downloads/data?format=geojson&spatialRefId=4326&where=1%3D1")
    with open(f"lar/data/{filename}.geojson", "wb") as f:
        f.write(response.content)

def main():
    for name, dataset in dataset_ids.items():
        download_datasets(name, dataset)

if __name__ == "__main__":
    main()
