
import nltk
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk

nltk.download('wordnet')
nltk.download('omw-1.4')

def disambiguate_word_sense(context_sentence, ambiguous_word):
    tokens = context_sentence.split()  # Using split instead of word_tokenize
    sense = lesk(tokens, ambiguous_word)
    return sense

# Example usage
sentence = "The bank was steep and difficult to climb."
word = "bank"
sense = disambiguate_word_sense(sentence, word)

if sense:
    print(f"Word: {word}")
    print(f"Sense: {sense.name()}")
    print(f"Definition: {sense.definition()}")
else:
    print("No sense found.")
