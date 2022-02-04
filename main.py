from fastapi import FastAPI
from generator_service.planet_generator import generate_planet
from generator_service.ship_generator import generate_ship
from generator_service.shop_generator import generate_shop

app = FastAPI()

@app.get("/ping")
def ping():
    return {"OK"}

@app.get("/planet")
def get_planet():
    generated_planet = generate_planet()
    return generated_planet

@app.get("/ship")
def get_ship():
    generated_ship = generate_ship()
    return generated_ship

@app.get("/shop")
def get_shop():
    generated_shop = generate_shop()
    return generated_shop
