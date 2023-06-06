# REST API Documentation

## Overview
This document describes the public RESTful API for accessing and manipulating data on our service. The API is designed to be simple and easy to use, with predictable and resource-oriented URLs.

## Base URL
All API requests should be made to the base URL such as: `http://127.0.0.1:5000`

## Resources
Our API provides access to several resources, including:

- **Index**: Returns a message indicating that the API is working.
- **Test**: Returns a message indicating that the API is working and includes the provided latitude value.
- **Locations**: Returns location data based on the provided latitude, longitude, radius, and database collections.

## Endpoints
Here are some example endpoints for our API:

- `GET /`: Returns a message indicating that the API is working.
- `GET /test/:lat`: Returns a message indicating that the API is working and includes the provided latitude value.
- `GET /locs/:lat,:lon,:radius/:dbs`: Returns location data based on the provided latitude, longitude, radius, and database collections.

## Request and Response Format
All requests and responses are in JSON format. Here's an example request to get location data:

```
GET /locs/-70.98471383,41.672747140,10000/Hospitals,FireStations
```

And here's an example response:

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "FIRESTATIONS": [
        {
            "geometry": {
                "coordinates": [-70.98281860299994, 41.63984680200008],
                "type": "Point"
            }
        },
        ...
    ],
    "HOSPITALS": [
        {
            "geometry": {
                "coordinates": [-70.98471383, 41.6727471400001],
                "type": "Point"
            }
        },
        ...
    ]
}
```
