from typing import Any, Dict, List
from src.database import client, paged_filtered_query, query_daily_pickups_per_neighborhood, query_unique_neighborhoods

def get_root():
    total = client.execute('SELECT count() FROM trips')

    return {
        "database": "default",
        "total": "Total registries %s" % str(total[0][0]),
        "docs-entrypoint": "/docs",
        "entrypoints": ["/trips","/trips/daily-by-neighborhood", "/neighborhoods"]
    }

def get_filtered_trips(
    filters: Dict[str,Any],
    page: int = 1,
    limit: int = 15
):
    results_tuple = paged_filtered_query(filters=filters,page=page,limit=limit)
    result = results_tuple[0]
    total_results = results_tuple[1]
    trips = []
    for row in result:
        trip = {
            "trip_id": row[0] ,
            "pickup_date": row[1],
            "pickup_ntaname": row[2],
            "passenger_count" : row[3],
            "trip_distance" : row[4],
            "tolls_amount" : row[5],
            "total_amount" : row[6],
        }
        trips.append(trip)
    return (trips, total_results)


def daily_pickups_per_neighborhood(
    filters: Dict[str,Any],
    page: int = 1,
    limit: int = 15
):
    results_tuple = query_daily_pickups_per_neighborhood(filters=filters,page=page,limit=limit)
    result = results_tuple[0]
    total_results = results_tuple[1]
    trips = []
    for row in result:
        trip = {
            "pickup_date": row[0],
            "pickup_ntaname" : row[1],
            "number_of_trips" : row[2],
            # Agrega más campos según la estructura de tu tabla
        }
        trips.append(trip)
    return (trips, total_results)

def unique_neighborhoods(
   
    page: int = 1,
    limit: int = 15
):
    results_tuple = query_unique_neighborhoods(page=page,limit=limit)
    result = results_tuple[0]
    total_results = results_tuple[1]
    neighborhoods = []
    for row in result:
        neighborhood = str(row[0]),
        neighborhoods.append(neighborhood)
    return (neighborhoods, total_results)
