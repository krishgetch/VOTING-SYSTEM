from fastapi import APIRouter, HTTPException
from database import db, cursor
import bcrypt

auth_router = APIRouter()

# Register a voter
@auth_router.post("/register")
def register(voter_id: str, password: str):
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    try:
        cursor.execute("INSERT INTO voters (voter_id, password) VALUES (%s, %s)", (voter_id, hashed_password))
        db.commit()
        return {"message": "Voter registered successfully!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Login a voter
@auth_router.post("/login")
def login(voter_id: str, password: str):
    cursor.execute("SELECT password FROM voters WHERE voter_id = %s", (voter_id,))
    voter = cursor.fetchone()
    
    if voter and bcrypt.checkpw(password.encode("utf-8"), voter[0].encode("utf-8")):
        return {"message": "Login successful!"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
