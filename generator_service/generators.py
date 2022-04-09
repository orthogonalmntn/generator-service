"""""
  Text generating models and helper functions
"""""

from transformers import pipeline

# Load & start up GPT-2
generator = pipeline('text-generation', model='gpt2')

# We can use a more capable generator of Description if needed, but it will generate slower:
# generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')