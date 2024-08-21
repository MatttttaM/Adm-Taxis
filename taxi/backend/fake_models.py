# from sqlalchemy import URL, Column, Integer, Float, String, DateTime, create_engine
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class User(Base):
#     __tablename__ = 'libro_diario'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     chofer_cod = Column(Integer, primary_key=True)
#     movil = Column(Integer, nullable=False)
#     total = Column(Integer)
#     gastos = Column(Integer)
#     salario = Column(Integer)
#     viatico = Column(Integer)
#     combustible = Column(Integer)
#     extras = Column(Integer)
#     liquido = Column(Integer)
#     aportes = Column(Float)
#     sub_total = Column(Float)
#     h13 = Column(Integer)
#     credito = Column(Integer)
#     fecha = Column(DateTime)
#     estado = Column(String(50))


# # Configuración de la base de datos
# # engine = create_engine(URL)
# # Base.metadata.create_all(engine)

# from sqlalchemy.engine import URL

# # url_object = URL.create(
# #     "mongodb+srv",
# #     username="mattbarbr",
# #     password="JDwlfWhN5nrW6xHN"
# #     host="admtaxis.z0eog.mongodb.net/",
# #     database="test",
# # )

# from sqlalchemy import create_engine

# # engine = create_engine(url_object)