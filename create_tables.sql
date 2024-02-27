-- Create the Author table
CREATE TABLE Author (
  id INTEGER PRIMARY KEY,
  name VARCHAR(150),
  article_count INTEGER
);

-- Create the Paper table
CREATE TABLE Paper (
  id INTEGER PRIMARY KEY,
  arxiv_id VARCHAR(20),
  year INTEGER,
  title VARCHAR(200),
  categories VARCHAR(20),
  abstract TEXT
);

-- Create the Author_Paper table
CREATE TABLE Author_Paper (
  id INTEGER PRIMARY KEY,
  author_id INTEGER,
  paper_id INTEGER,
  FOREIGN KEY (author_id) REFERENCES Author(id),
  FOREIGN KEY (paper_id) REFERENCES Paper(id)
);

-- Create User table for authentification
CREATE TABLE UserApiData (
  id VARCHAR(255) PRIMARY KEY,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(60) NOT NULL
);

CREATE TABLE UserApiModel (
  id VARCHAR(255) PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(60) NOT NULL
);
