from db import filmconnection
from bson.objectid import ObjectId
from datetime import datetime
import json

def film_schema(film)->dict:
    return {"id": str(film["_id"]),
            "title": film["title"],
            "director": film["director"],
            "year": film["year"],
            "genere": film["genre"],
            "rating": film["rating"],
            "country": film["country"],
            "created_at": film["created_at"],
            "updated_at": film["updated_at"]
    }
    
def films_schema(films) ->dict:
    return[film_schema(film) for film in films]

    
def getAllFilms():
    try:    
        conn = filmconnection.db()
        data = conn.films.find()
        
    
        films = [film_schema(film) for film in data]
        if films:
            result = {
                "status": 1,
                "data": films
            }
        else:
            result = {
                "status": -1,
                "message": "Cap pel·lícula trobada"
            }
        return result
    
    except Exception as e:
        return {
            "status": -1,
            "message": f'Error de connexió: {e}'
        }

def getFilmById(id):
    try:    
        conn = filmconnection.db()
        data = conn.films.find_one({"_id" : ObjectId(id)})
        if data:
            result = {
                "status": 1,
                "data": film_schema(data)
            }
        else:
            result = {
                "status": -1,
                "message": "Cap pel·lícula trobada"
            }
        return result
    except Exception as e:
        return {
            "status": -1,
            "message": f'Error de connexió: {e}'
        }

def createFilm(new_film_data):
    try:
        conn = filmconnection.db()
        now = datetime.now()
        data = {
            "title": new_film_data.title,
            "director": new_film_data.director,
            "year": new_film_data.year,
            "genre": new_film_data.genre,
            "rating": new_film_data.rating,
            "country": new_film_data.country,
            "created_at": now,
            "updated_at": now
        }
        id = conn.films.insert_one(data).inserted_id
        
        response = {
            "status": 1,
            "data": {
                "id": str(id)
                }
        }
        
        return response
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió: {e}"}

def updateFilm(id, updateFilm):
    try:
        conn = filmconnection.db()
        now = datetime.now()
        data={
            "title": updateFilm.title,
            "director": updateFilm.director,
            "year": updateFilm.year,
            "genre": updateFilm.genre,
            "rating": updateFilm.rating,
            "country": updateFilm.country,
            "updated_at": now
        }  
        conn.films.update_one({"_id" : ObjectId(id)}, {"$set": data})
        response = {
                "status": 1,
                "data": {
                    "id": id
                }
            }
        return response
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió: {e}"}
    
def deleteFilm(id):
    try:
        conn = filmconnection.db()
        result = conn.films.delete_one({"_id": ObjectId(id)})
        
        if result.deleted_count > 0:
            return {"status": 1, "message": "La pel·lícula s'ha esborrat correctament"}
        else:
            return {"status": -1, "message": "La pel·lícula no s'ha trobat a la BBDD"}
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió: {e}"}