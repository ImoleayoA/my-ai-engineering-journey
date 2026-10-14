from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import User, Document


router = APIRouter(prefix="/documents", tags=["documents"])


class DocumentCreate(BaseModel):
    title: str
    content: str
    user_id: int


class DocumentResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int

    class Config:
        from_attributes = True


@router.get("/", response_model=list[DocumentResponse])
def list_documents(db: Session = Depends(get_db)):
    return db.query(Document).all()


@router.get("/user/{user_id}", response_model=list[DocumentResponse])
def list_user_documents(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.documents


@router.post("/", response_model=DocumentResponse, status_code=201)
def create_document(doc: DocumentCreate, db: Session = Depends(get_db)):
    user = db.get(User, doc.user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    new_doc = Document(
        title=doc.title,
        content=doc.content,
        user_id=doc.user_id
    )
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc
