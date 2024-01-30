from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Paper, Author

app = FastAPI()


@app.get("/api/papers/{paper_id}")
async def get_paper(paper_id, db: Session = Depends(get_db)):
    data = db.query(Paper).filter(Paper.id == paper_id).first()
    return data


@app.get("/api/authors/{author_id}")
async def get_author(author_id, db: Session = Depends(get_db)):
    data = db.query(Author).filter(Author.id == author_id).first()
    return data
