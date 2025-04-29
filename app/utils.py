from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)
#print("utils.py loaded")

def verify(plainpwd,hashedpwd):
    return pwd_context.verify(plainpwd,hashedpwd)