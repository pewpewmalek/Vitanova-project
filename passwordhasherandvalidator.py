from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plain: str) -> str:
    return pwd_context.hash(plain)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

# Test
password = "VNIAS@2026"
hashed = hash_password(password)

print("Hash:", hashed)
print("Verify Correct:", verify_password("VNIAS@2026", hashed)) # True
print("Verify Wrong:", verify_password("wrongpass", hashed)) # False