import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.middleware.cors import CORSMiddleware

from dark_innotech.schemas import Contact as ContactSchema
from dark_innotech.database import get_db
from dark_innotech.models import Contact as ContactModel

app = FastAPI()

# Allow requests from Django (or adjust origin if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],  # Django runs at 8000 by default
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/contact")
async def receive_contact(contact: ContactSchema, db: AsyncSession = Depends(get_db)):
    new_contact = ContactModel(**contact.dict())
    db.add(new_contact)
    await db.commit()
    await db.refresh(new_contact)
    return {"message": "Thank you for reaching out!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
