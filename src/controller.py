from typing import Any, Dict, List

from fastapi import Query
from .database import client

def get_paginated_trips(page: int = 1, limit: int = 15) -> List[Dict[str, Any]]:

    # Calcula el offset según la página y el límite
    offset = (page - 1) * limit
    # Ejecuta la consulta paginada y ordenada por pickup_date
 
    query = "SELECT trip_id, pickup_date, dropoff_date, pickup_ntaname FROM trips ORDER BY pickup_date ASC LIMIT %d OFFSET %d" % (limit, offset)
    
    result = client.execute(query)

    total_results = client.execute("SELECT COUNT() FROM trips")
    # Mapea los resultados a un formato más amigable
    trips = []
    for row in result:
        trip = {
            "trip_id": row[0],
            "pickup_date": row[1],
            "dropoff_date": row[2],
            "pickup_ntaname" : row[3],
            
            # Agrega más campos según la estructura de tu tabla
        }
        trips.append(trip)


    return (trips, total_results[0][0])

def get_filtered_trips_by_location(
    pickup_ntaname: str,
    page: int =1,
    limit: int =15
):
    # Construye la consulta SQL utilizando los parámetros de ruta y de consulta
    query = 'SELECT trip_id, pickup_date, dropoff_date, pickup_ntaname  FROM trips WHERE pickup_ntaname = %s' % pickup_ntaname
    
    offset = (page - 1) * limit

    # Agrega la ordenación y la paginación
    query += ' ORDER BY pickup_date ASC LIMIT %d OFFSET %d' % (limit,offset)
   

    # Ejecuta la consulta con los parámetros
    result = client.execute(query)
    trips = []
    for row in result:
        trip = {
            "trip_id": row[0],
            "pickup_date": row[1],
            "dropoff_date": row[2],
            "pickup_ntaname" : row[3],
            
            # Agrega más campos según la estructura de tu tabla
        }
        trips.append(trip)
    total_results = client.execute("SELECT COUNT() FROM trips WHERE pickup_ntaname = %(pickup_ntaname)s AND pickup_date = %s")

    # Procesa los resultados como desees y devuelve la respuesta
    # Aquí debes procesar los resultados y devolver la respuesta según tu lógica de negocio

    return (trips, total_results[0][0])