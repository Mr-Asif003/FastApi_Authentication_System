from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

from app.models.user import User

from app.repositories.user_repository import (
    UserRepository
)


class AuthService:

    def __init__(self, db: Session):

        self.user_repository = UserRepository(db)

    def register(
        self,
        email: str,
        username: str,
        password: str
    ):

        existing_email = (
            self.user_repository.get_by_email(email)
        )

        if existing_email:

            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered"
            )

        existing_username = (
            self.user_repository.get_by_username(username)
        )

        if existing_username:

            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Username already registered"
            )

        user = User(
            email=email,
            username=username,
            hashed_password=hash_password(password),
            role="user",
            is_active=True
        )

        return self.user_repository.create(user)

    def login(
        self,
        email: str,
        password: str
    ):

        user = self.user_repository.get_by_email(email)

        if not user:

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        if not verify_password(
            password,
            user.hashed_password
        ):

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        if not user.is_active:

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User account is inactive"
            )

        token = create_access_token({
            "sub": str(user.id),
            "role": user.role
        })

        return token