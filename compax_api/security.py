from passlib.context import CryptContext


class Password:
    context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def verify(plain: str, hashed: str):
        return Password.context.verify(secret=plain, hash=hashed)

    @staticmethod
    def hash(password: str):
        return Password.context.hash(secret=password)
