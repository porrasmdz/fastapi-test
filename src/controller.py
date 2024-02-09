from typing import Any, Dict, List

from fastapi import Query
from .database import client, paged_filtered_query



def get_filtered_trips(
    filters: Dict[str,Any],
    page: int = 1,
    limit: int = 15
):
    results_tuple = paged_filtered_query(filters=filters,page=page,limit=limit)
    print("Tupla resultante: ",str(results_tuple))
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