# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lKz3iFj9Kaf4j4ez6FzUjxFrjZNABQJZ
"""

pip install rdflib

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

# Crea un grafo RDF
g = Graph()

# Define un espacio de nombres para nuestra ontología
ontologia = Namespace("http://www.ejemplo.com/ontologia#")

# Define clases y propiedades
g.add((ontologia.Persona, RDF.type, RDFS.Class))
g.add((ontologia.tieneEdad, RDF.type, RDF.Property))

# Agrega instancias y relaciones
g.add((ontologia.Juan, RDF.type, ontologia.Persona))
g.add((ontologia.Juan, ontologia.tieneEdad, Literal(30)))

# Consulta la ontología
for subj, pred, obj in g:
    print(f"Sujeto: {subj}, Predicado: {pred}, Objeto: {obj}")

