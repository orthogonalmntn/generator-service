from typing import Optional
from fastapi import FastAPI, Header, HTTPException

from generator_service.planet_generator import generate_planet
from generator_service.ship_generator import generate_ship
from generator_service.shop_generator import generate_shop

from generator_service.jwt_service import verify_token
import jwt
app = FastAPI()

@app.get("/ping")
def ping():
    return {"OK"}

@app.get("/planet")
def get_planet(x_token: Optional[str] = Header(None)):
    try:
      verify_token(x_token)
    except jwt.exceptions.InvalidSignatureError:
      raise HTTPException(status_code=403, detail="Access denied")

    generated_planet = generate_planet()
    return generated_planet

@app.get("/ship")
def get_ship(x_token: Optional[str] = Header(None)):
    try:
      verify_token(x_token)
    except jwt.exceptions.InvalidSignatureError:
      raise HTTPException(status_code=403, detail="Access denied")

    generated_ship = generate_ship()
    return generated_ship

@app.get("/shop")
def get_shop(x_token: Optional[str] = Header(None)):
    try:
      verify_token(x_token)
    except jwt.exceptions.InvalidSignatureError:
      raise HTTPException(status_code=403, detail="Access denied")

    generated_shop = generate_shop()
    return generated_shop
