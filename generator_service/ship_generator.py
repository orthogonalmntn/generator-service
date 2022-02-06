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
  while True:
    try:
      attempt = generate_ship_name()
    except KeyError:
      continue

    if attempt:
      return max(attempt, key=len)

def try_generate_ship_description(ship_name):
  output = generator(f"The space ship {ship_name} can be described as", do_sample=True, min_length=50)
  sentences = [str(i) for i in nlp(output[0]["generated_text"]).sents]

  sentences.pop() # remove last dangling sentence.
  joined_sentences = ''.join(sentences)

  return joined_sentences

def compound_names_based_on_ent_iob(names):
    compounded_names = {}
    i = 0

    for name in names:
        if name[1] == 3:
            compounded_names[i] = name[0]
        if name[1] == 1:
            compounded_names[i] = compounded_names[i] + " " + name[0]
        if name[1] == 2:
            i += 1
    return list(compounded_names.values())

def generate_ship_name():
    prompt = "A science-fictional name for an alien space ship is"
    output = generator(prompt, max_length=20, num_return_sequences=5)

    forbidden_ship_names = ('USS', 'Star Trek', 'Star Wars', 'TARDIS', 'Enterprise')

    all_generated_ships = []

    for item in output:
        text_to_extract = item['generated_text']
    
        doc = nlp(text_to_extract)
        ship_names = [(token.lemma_, token.ent_iob) for token in doc if token.pos_ == "PROPN"]
        compound_names = compound_names_based_on_ent_iob(ship_names)

        sanitized_list = [e for e in compound_names if e not in forbidden_ship_names]

        if len(sanitized_list) > 0:
            all_generated_ships.append(sanitized_list)
    
    flat_list_of_ships = [item for sublist in all_generated_ships for item in sublist]
    return flat_list_of_ships