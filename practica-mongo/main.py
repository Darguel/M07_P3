from typing import Union
from fastapi import FastAPI
from model import film
from db import filmpeticions

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/films")
def getFilms():
    return filmpeticions.getAllFilms()

@app.get("/films/{id}")
def getFilmById(id):
    return filmpeticions.getFilmById(id)

@app.post("/film/")
def createFilm(film: film.Film):
    return filmpeticions.createFilm(film)

@app.put("/film/{id}")
def updateFilm(id, film: film.Film):
    return filmpeticions.updateFilm(id, film)
30
@app.delete("/film/{id}")
def deleteFilm(id):
    return filmpeticions.deleteFilm(id)
