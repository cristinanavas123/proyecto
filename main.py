"""
imagina que esta es API es una bibiloteca de peliculas:
La funcion load_movies() es como una biblioteca que carga el catalogo de libros (peliculas) cuando se abre la biblioteca
La función get_movies() muestra todo el catalogo cuando alguien lo pide.
la funcion get_movie(id) es como si alguien preguntara por un libro especifico. es decir por su codigo de identificación
la funcion chatbot(query) es un asistente que busca películas según palabras clave y sinónimo.
La función get_movies_by_category(category) ayuda a encontrar peliculas segun su genero (acción. comedia, etc)
"""

# importamos las herramientas necesarias para continuar nuestra API
from fastapi import FastAPI, HTTPException # fastAPI nos ayuda a crear la API, HTTExcepcion nos ayuda a  manejar errores.
from fastapi.responses import HTMLResponse, JSONResponse # HTMLResponse nos ayuda a manejar respuestas HTML, y JSONResponse nos ayuda a manejar respuestas en formato JSON
import pandas as pd # pandas nos ayuda a manejar datos en tablas como si fuera un excel.
import nltk # es una libreria para procesar textos y analizar palabras
from nltk.tokenize import word_tokenize # word_tokenize nos ayuda a tokenizar teto, es decir a convertirlo en palabras
from nltk.corpus import wordnet # wordnet es una libreria para analizar sinónimos

# indicamos la ruta donde nltk buscará los datos descargados en nuestro computador
nltk.data.path.append('C:\Users\lucia\AppData\Roaming\nltk_data')
nltk.download('punkt')

