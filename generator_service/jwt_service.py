"""""
  JWT verifiers
"""""

import jwt
from fastapi import HTTPException
import os

ALGORITHM = "HS512"
SECRET_KEY = os.environ["JWT_SECRET_KEY"]

def verify_token(token):
  try:
    jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
  except jwt.exceptions.InvalidTokenError:
    raise HTTPException(status_code=403, detail="Access denied")