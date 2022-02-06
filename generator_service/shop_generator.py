from generator_service.generators import generator
from generator_service.nlp import nlp, compound_names_based_on_ent_iob, join_sentences

class Shop:
  def __init__(self, name, description):
    self.name = name
    self.description = description

def generate_shop():
  shop_name = try_generate_shop_name()
  shop_description = try_generate_shop_description(shop_name)
  return Shop(shop_name, shop_description)

def try_generate_shop_name():
  while True:
    try:
      attempt = generate_shop_name()
    except KeyError:
      continue

    if attempt:
      return max(attempt, key=len)

def try_generate_shop_description(shop_name):
  output = generator(f"The merchandise shop in space {shop_name} can be described as", do_sample=True, min_length=50)
  return join_sentences(output)

def generate_shop_name():
    prompt = "A science-fictional name for an alien shop selling merchandise in space is"
    output = generator(prompt, max_length=20, num_return_sequences=5)

    forbidden_shop_names = ('Star', 'Star Trek', 'Star Wars', 'TARDIS', 'Enterprise')

    all_generated_shops = []

    for item in output:
        text_to_extract = item['generated_text']
    
        doc = nlp(text_to_extract)
        shop_names = [(token.lemma_, token.ent_iob) for token in doc if token.pos_ == "PROPN"]
        compound_names = compound_names_based_on_ent_iob(shop_names)

        sanitized_list = [e for e in compound_names if e not in forbidden_shop_names]

        if len(sanitized_list) > 0:
            all_generated_shops.append(sanitized_list)
    
    flat_list_of_shops = [item for sublist in all_generated_shops for item in sublist]
    return flat_list_of_shops