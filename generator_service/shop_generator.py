from generator_service.generators import nlp, generator

class Shop:
  def __init__(self, name, description):
    self.name = name
    self.description = description

def generate_shop():
  shop_name = try_generate_shop_name()
  shop_description = try_generate_shop_description(shop_name)
  return Shop(shop_name, shop_description)

def try_generate_shop_name():
  return "Shop Name"

def try_generate_shop_description(shop_name):
  return f"Shop Description for {shop_name}"