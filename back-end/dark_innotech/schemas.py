
from pydantic import BaseModel



class Contact(BaseModel):
    name: str
    email: str
    subject: str
    message: str