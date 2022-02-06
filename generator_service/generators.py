"""""
  Text generating models and helper functions
"""""

from transformers import pipeline

# Load & start up GPT-2
generator = pipeline('text-generation', model='gpt2')

# We can use different generators of Description if needed:
# generator_2 = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')