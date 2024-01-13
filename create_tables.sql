-- Create the Author table
CREATE TABLE Author (
  id INTEGER PRIMARY KEY,
  name VARCHAR(150),
  article_count INTEGER
);

-- Create the Paper table
CREATE TABLE Paper (
  id INTEGER PRIMARY KEY,
  year INTEGER,
  title VARCHAR(200),
  source VARCHAR(5),
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
