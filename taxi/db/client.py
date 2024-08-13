from sqlmodel import SQLModel, create_engine

DB_URL = "mysql+pymysql://root:Admin@localhost:3306/taxidb"

# Conectar a la base de datos MySQL
engine = create_engine(DB_URL)

# Crear todas las tablas basadas en los modelos
SQLModel.metadata.create_all(engine)


# from pymongo import MongoClient

# Base de datos local
# db_client = MongoClient().local

# Base de datos remota
# python -m pip install "pymongo[srv]"==3.11


# db_client = MongoClient("mongodb+srv://mattbarbr:JDwlfWhN5nrW6xHN@admtaxis.z0eog.mongodb.net/".test)