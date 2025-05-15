"""
imagina que esta es API es una bibiloteca de peliculas:
La funcion load_movies() es como una biblioteca que carga el catlogo de libros (peliculas) cuando se abre la biblioteca
Lafunción get_movies() muestra todo el catalogo cuando alguien lo pide
la funcion get_movie(id) es como si alguien preguntara por un libro especifico por su codigo de identificación
la funcion chatbot (query) es un asistente que busca libros según papalabras clave y sinónimo.
La función get_movies_by_category (cagory) ayuda a encontrar peliculas segun su genero (acción. comeia, etc)
"""

# importamos las herramientas necesarias para constuir un API
from fastapi import FastAPI, HTTPException # fastAPI nos ayuda a crear la API, HTTexcepcion maneja errores.
from fastapi.responses