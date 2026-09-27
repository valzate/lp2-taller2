"""
Extensiones de Flask.

La instancia de SQLAlchemy se crea en un archivo aparte para evitar
importaciones circulares: models.py necesita 'db', y __init__.py necesita
tanto 'db' como los modelos. Teniéndola aquí, ambos pueden importarla sin
depender el uno del otro.
"""

from flask import app
from flask_sqlalchemy import SQLAlchemy

from app import create_app

# Instancia global del ORM. Todavía no está ligada a ninguna aplicación:
# eso ocurre en create_app() con db.init_app(app).
app = create_app()
db = SQLAlchemy()
db.init_app(app)

