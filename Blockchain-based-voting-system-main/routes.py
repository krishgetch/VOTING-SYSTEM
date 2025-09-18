from fastapi import APIRouter, HTTPException
from database import db, cursor
from auth import auth_router

router = APIRouter()

# Include authentication routes
router.include_router(auth_router, prefix="/auth")

# Get candidates
@router.get("/candidates")
def get_candidates():
    cursor.execute("SELECT * FROM candidates")
    return cursor.fetchall()

# Add a candidate
@router.post("/candidates")
def add_candidate(name: str, party: str):
    try:
        cursor.execute("INSERT INTO candidates (name, party) VALUES (%s, %s)", (name, party))
        db.commit()
        return {"message": "Candidate added successfully!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Cast a vote
@router.post("/vote")
def cast_vote(voter_id: str, candidate_id: int):
    try:
        cursor.execute("INSERT INTO votes (voter_id, candidate_id) VALUES (%s, %s)", (voter_id, candidate_id))
        db.commit()
        return {"message": "Vote cast successfully!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Get voting results
@router.get("/results")
def get_results():
    cursor.execute("SELECT candidate_id, COUNT(*) as votes FROM votes GROUP BY candidate_id")
    return cursor.fetchall()
