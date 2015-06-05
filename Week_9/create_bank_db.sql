DROP TABLE IF EXISTS Clients;

CREATE TABLE Clients(
  client_id INTEGER PRIMARY KEY,
  username TEXT UNIQUE,
  password TEXT,
  balance REAL DEFAULT 0,
  message TEXT,
  email TEXT,
  hash TEXT,
  failed_logins INTEGER DEFAULT 0,
  last_failed_login INTEGER
);
