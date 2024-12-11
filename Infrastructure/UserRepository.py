from sqlalchemy.orm import Session
from Entities.User import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def find_by_email(self, email: str) -> User:
        return self.session.query(User).filter_by(email=email).first()

    def save(self, user: User) -> None:
        self.session.add(user)
        self.session.commit()
