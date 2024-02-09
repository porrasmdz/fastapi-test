from typing import Any, Dict, List

from fastapi import Query
from .database import paged_filtered_query, query_daily_pickups_per_neighborhood


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
            "dropoff_date": row[2],
            "pickup_ntaname" : row[3],
            # Agrega más campos según la estructura de tu tabla
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