from generator_service.generators import generator
from generator_service.nlp import nlp, compound_names_based_on_ent_iob, join_sentences

class Planet:
  def __init__(self, name, description):
    self.name = name
    self.description = description

def generate_planet():
  planet_name = try_generate_planet_name()
  planet_description = try_generate_planet_description(planet_name)
  return Planet(planet_name, planet_description)

def try_generate_planet_name():
  while True:
    try:
      attempt = generate_planet_name()
    except KeyError:
      continue

    if attempt:
      return max(attempt, key=len)

def try_generate_planet_description(planet_name):
  output = generator(f"The planet {planet_name} can be described as", do_sample=True, min_length=50)
  return join_sentences(output)

def generate_planet_name():
    prompt = "A creative name for a planet outside our Solar System is"
    output = generator(prompt, max_length=20, num_return_sequences=5)

    forbidden_planet_names = ('Solar System', 'Solar' 'System', 'Earth', 'Mars', 'Mercury',
                              'Neptune', 'Saturn', 'Jupiter', 'Pluto', 'Uranus',
                              'Sun', 'Milky', 'Way', 'Moon', 'Asteroid', 'International',
                              'Astronomical', 'Union', 'Planet', 'Planets', 'Fermi', 
                              'Paradox', 'Europa', 'Venus', 'Universe', 'Red Planet', 
                             'Deep Space', 'Pleiades', 'Asteroids', 'Jovian', 'Kepler')

    all_generated_planets = []

    for item in output:
        text_to_extract = item['generated_text']
        text_to_extract = text_to_extract.replace(prompt, "")
    
        doc = nlp(text_to_extract)
            
        planet_names = [(token.lemma_, token.ent_iob) for token in doc if token.pos_ == "PROPN"]
        compound_names = compound_names_based_on_ent_iob(planet_names)
    
        sanitized_list = [e for e in compound_names if e not in forbidden_planet_names]

        if len(sanitized_list) > 0:
            all_generated_planets.append(sanitized_list)
    
    flat_list_of_planets = [item for sublist in all_generated_planets for item in sublist]
    return flat_list_of_planets
