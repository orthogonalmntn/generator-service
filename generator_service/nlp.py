"""""
  NLP libraries and helper functions
"""""

import spacy

# Load up SpaCy language model
nlp = spacy.load("en_core_web_sm")

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

def join_sentences(output_from_text_model):
  sentences = [str(i) for i in nlp(output_from_text_model[0]["generated_text"]).sents]

  sentences.pop() # remove last dangling sentence.
  joined_sentences = ''.join(sentences)

  return joined_sentences