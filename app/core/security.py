from datetime import datetime,timedelta,timezone

from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.util import deprecated

from app.core.config import settings

pwd_context=CryptContext(
    schemes=["bcrypt"],
    deprecated='auto'
)

def hash_password(password:str)->str:
    return pwd_context.hash(password)

def verify_password(
        plain_passwoord:str,
        hash_password:str
)->bool:
    return pwd_context.verify(plain_passwoord,hash_password)

def create_access_token(
        data:dict,
        expires_delta:timedelta|None=None
):
    payload=data.copy()

    if expires_delta:
        expire=datetime.now(timezone.utc)+expires_delta

    else:
        expire=(
            datetime.now(timezone.utc)
            +timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        )
    payload.update({
        "exp":expire,
        "iat":datetime.now(timezone.utc)
    })
    token=jwt.encode(
        payload,
        settings.JWT_SECTRET_KEY,
        algorithm=settings.JWT_AlGORITHM
    )
    return token
