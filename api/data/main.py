from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Paper, Author

app = FastAPI(debug=True)


@app.get("/api/papers/{skip}:{limit}")
async def get_papers_batch(skip, limit, db: Session = Depends(get_db)):
    data = db.query(Paper).offset(skip).limit(limit).all()
    return data


@app.get("/api/papers/{paper_id}")
async def get_paper(paper_id, db: Session = Depends(get_db)):
    data = db.query(Paper).filter(Paper.id == paper_id).first()
    return data


@app.get("/api/authors/{skip}:{limit}")
async def get_authors_batch(skip, limit, db: Session = Depends(get_db)):
    data = db.query(Author).offset(skip).limit(limit).all()
    return data


@app.get("/api/authors/{author_id}")
async def get_author(author_id, db: Session = Depends(get_db)):
    data = db.query(Author).filter(Author.id == author_id).first()
    return data
