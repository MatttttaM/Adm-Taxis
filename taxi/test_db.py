import pymysql


timeout = 10
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host="dbliqudiaciones-admtaxi.b.aivencloud.com",
    password="AVNS_0wDZLak0nK19kamQus8",
    read_timeout=timeout,
    port=16928,
    user="avnadmin",
    write_timeout=timeout,
)



# try:
#     cursor = connection.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS liquidaciones (
#             chofer INTEGER PRIMARY KEY,
#             movil INTEGER,
#             recaudacion INTEGER NOT NULL,
#             combustible INTEGER,
#             extras INTEGER,
#             salario DECIMAL(10, 2),
#             gastos DECIMAL(10, 2),
#             liquido DECIMAL(10, 2),
#             h13 INTEGER,
#             credito INTEGER,
#             entrega DECIMAL(10, 2),
#             fecha VARCHAR(50),
#             estado VARCHAR(50));
#         """)
#     connection.commit()

# finally:
#     connection.close()


cursor = connection.cursor()

#cursor.execute("ALTER TABLE liquidaciones ADD COLUMN aportes INTEGER after salario;")
#cursor.execute("ALTER TABLE liquidaciones ADD COLUMN sub_total DECIMAL(10,2) AFTER salario;")
#cursor.execute("ALTER TABLE liquidaciones modify sub_total DECIMAL(10,2) AFTER aportes;")
#cursor.execute("ALTER TABLE liquidaciones modify aportes DECIMAL(10,2) AFTER liquido ;")
#cursor.execute("ALTER TABLE liquidaciones ADD COLUMN cod_id 
#cursor.execute("SELECT * FROM liquidaciones;")
#print(cursor.fetchall())
#connection.commit()
#cursor.execute("ALTER TABLE liquidaciones DROP PRIMARY KEY, ADD PRIMARY KEY (cod_id);")
#cursor.execute("TRUNCATE TABLE liquidaciones")


connection.commit()
