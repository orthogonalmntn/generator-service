from generator_service.generators import nlp, generator

class Ship:
  def __init__(self, name, description):
    self.name = name
    self.description = description

def generate_ship():
  ship_name = try_generate_ship_name()
  ship_description = try_generate_ship_description(ship_name)
  return Ship(ship_name, ship_description)

def try_generate_ship_name():
  return "Shop Name"

def try_generate_ship_description(ship_name):
  return f"Ship Description for {ship_name}"