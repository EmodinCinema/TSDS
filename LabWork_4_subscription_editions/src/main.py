import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from pydantic.class_validators import List
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.database import SessionLocal, engine
from src.models import Subscription

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    """
    Задаем зависимость к БД. При каждом запросе будет создаваться новое
    подключение.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/recipient/", response_model=schemas.Recipient)
def create_user(recipient: schemas.RecipientCreate, db: Session = Depends(get_db)):
    """
    Создание Подпищика, если такой recipient codee уже есть в БД, то выдается ошибка
    """
    db_recipient = crud.get_recipient_by_code(db, recipient_code=recipient.recipient_code)
    if db_recipient:
        raise HTTPException(status_code=400, detail="Recipient already registered")
    return crud.create_recipient(db=db, recipient=recipient)


@app.post("/edition/", response_model=schemas.Edition)
def create_user(edition: schemas.EditionCreate, db: Session = Depends(get_db)):
    """
    Создание Издания, если такой edition codee уже есть в БД, то выдается ошибка
    """
    db_edition = crud.get_edition(db, index_edition=edition.index_of_the_publication)
    if db_edition:
        raise HTTPException(status_code=400, detail="Edition already registered")
    return crud.create_recipient(db=db, edition=edition)


@app.post("/subscription/", response_model=schemas.Subscription)
def create_subscription(subscription: schemas.SubscriptionCreate, recipient_id: int, edition_id: int, db: Session = Depends(get_db)):
    """
    Создание Подписки
    """
    db_recipient = crud.get_recipient(db, recipient_id=recipient_id)
    if not db_recipient:
        raise HTTPException(status_code=400, detail="Recipient not found")
    db_edition = crud.get_edition(db, edition_id=edition_id)
    if not db_edition:
        raise HTTPException(status_code=400, detail="Edition not found")
    return crud.create_subscription(db=db, subscription=subscription, recipient_id=recipient_id, edition_id=edition_id)


@app.post("/recipient/{recipient_id}", response_model=schemas.Recipient)
def read_recipient(recipient_id: int, db: Session = Depends(get_db)):
    """
    Получение Подпищика по id, если такой id уже есть в БД, то выдается ошибка
    """
    db_recipient = crud.get_recipient(db, recipient_id=recipient_id)
    if db_recipient is None:
        raise HTTPException(status_code=400, detail="Recipient not found")
    return db_recipient


@app.get("/edition/{edition_id}", response_model=schemas.Edition)
def read_edition(edition_id: int, db: Session = Depends(get_db)):
    """
    Получение Издания по id, если такой id уже есть в БД, то выдается ошибка
    """
    db_edition = crud.get_edition(db, edition_id=edition_id)
    if db_edition is None:
        raise HTTPException(status_code=400, detail="Recipient not found")
    return db_edition


@app.get("/recipient_subscription/{recipient_id}", response_model=list[schemas.Subscription])
def read_recipient_subscription(recipient_id: int, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    """
    Получение Подписки Подпищика по id, если такой id уже есть в БД, то выдается ошибка
    """
    db_subscription = crud.get_subscription_by_recipient(db=db, recipient_id=recipient_id, skip=skip, limit=limit)
    if db_subscription is None:
        raise HTTPException(status_code=400, detail="Recipient subscription not found")
    return db_subscription


@app.get("/edition_subscription/{recipient_id}", response_model=list[schemas.Subscription])
def read_recipient_subscription(edition_id: int, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    """
    Получение Подписки на Издания по id, если такой id уже есть в БД, то выдается ошибка
    """
    db_subscription = crud.get_subscription_by_edition(db=db, edition_id=edition_id, skip=skip, limit=limit)
    if db_subscription is None:
        raise HTTPException(status_code=400, detail="Edition subscription not found")
    return db_subscription


@app.get("/subscription/{subscription_id}", response_model=schemas.Subscription)
def read_recipient_subscription(subscription_id: int, db: Session = Depends(get_db)):
    """
    Получение Подписки на Издания по id, если такой id уже есть в БД, то выдается ошибка
    """
    db_subscription = crud.get_subscription(db, subscription_id=subscription_id)
    if db_subscription is None:
        raise HTTPException(status_code=400, detail="Subscription not found")
    return db_subscription


if __name__ == "__main__":
    uvicorn.run("main:app", port=6000, log_level="info", reload=True)