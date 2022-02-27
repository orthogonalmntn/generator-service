"""""
  JWT verifiers
"""""

import jwt
from fastapi import HTTPException

def verify_token(token):
  secret_key = "SOME_SECRET_KEY"
  algorithm = "HS512"

  try:
    jwt.decode(token, secret_key, algorithms=[algorithm])
  except jwt.exceptions.InvalidTokenError:
    raise HTTPException(status_code=403, detail="Access denied")