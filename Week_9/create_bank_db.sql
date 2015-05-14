DROP TABLE IF EXISTS Clients;

CREATE TABLE Clients(
  client_id INTEGER PRIMARY KEY,
  username TEXT UNIQUE,
  password TEXT,
  balance REAL DEFAULT 0,
  message TEXT
);
