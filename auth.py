from fastapi import Header, HTTPException, status

VALID_TOKENS = {"token_secretoooo"}

def authenticate_user(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid auth header")

    token = authorization.split(" ")[1]
    if token not in VALID_TOKENS:
        raise HTTPException(status_code=401, detail="Unauthorized")