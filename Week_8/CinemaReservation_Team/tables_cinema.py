import sqlite3


connection = sqlite3.connect("cinema.db")
cursor = connection.cursor()


CREATE_MOVIES_TABLE = """
CREATE TABLE IF NOT EXISTS Movies(
    id INTEGER PRIMARY KEY,
    name TEXT,
    rating REAL
)
"""


CREATE_PROJECTIONS_TABLE = """
CREATE TABLE IF NOT EXISTS Projections(
    proj_id INTEGER PRIMARY KEY,
    movie_id INTEGER,
    type TEXT,
    date TEXT,
    time TEXT,
    FOREIGN KEY(movie_id) REFERENCES Movies(id)
)
"""

CREATE_RESERVATION_TABLE = """
CREATE TABLE IF NOT EXISTS Reservations(
    reservation_id INTEGER PRIMARY KEY,
    username TEXT,
    projection_id INTEGER,
    row INTEGER,
    col INTEGER,
    FOREIGN KEY(projection_id) REFERENCES Projections(proj_id)
)
"""


for tables_cinema in [CREATE_MOVIES_TABLE, CREATE_PROJECTIONS_TABLE, CREATE_RESERVATION_TABLE]:
    cursor.execute(tables_cinema)

connection.commit()

connection.close()
