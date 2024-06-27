from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.counter import Counter

router = APIRouter()

@router.get("/")
def read_counter(db: Session = Depends(get_db)):
    counter = db.query(Counter).first()
    return {"count": counter.value if counter else 0}

@router.post("/")
def increment_counter(db: Session = Depends(get_db)):
    counter = db.query(Counter).first()
    if counter:
        counter.value += 1
    else:
        counter = Counter(value=1)
        db.add(counter)
    db.commit()
    db.refresh(counter)
    return {"count": counter.value}