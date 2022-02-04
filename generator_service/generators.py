import spacy
from transformers import pipeline

# Load up SpaCy language model
nlp = spacy.load("en_core_web_sm")

# Load & start up GPT-2
generator = pipeline('text-generation', model='gpt2')

# We can use different generators of Description if needed:
# generator_2 = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')