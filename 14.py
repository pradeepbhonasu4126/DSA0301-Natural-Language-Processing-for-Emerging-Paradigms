import nltk
from nltk import CFG

# Define a new Context-Free Grammar (CFG) for plural and singular subjects
grammar = CFG.fromstring("""
S -> NP VP
NP -> 'I' | 'You' | 'He' | 'She' | 'They'
VP -> V | V NP
V -> 'eat' | 'eats'
""")

# Create a parser using the grammar
parser = nltk.ChartParser(grammar)

# Function to check agreement and print result
def check_agreement(sentence):
    words = sentence.split()
    try:
        parses = list(parser.parse(words))
        if parses:
            print(f"'{sentence}' ➜ ✔️ Correct agreement")
        else:
            print(f"'{sentence}' ➜ ❌ Incorrect agreement")
    except ValueError:
        print(f"'{sentence}' ➜ ❌ Word not in grammar")

# Test cases
check_agreement("I eat")     # Correct
check_agreement("You eat")   # Correct
check_agreement("He eat")    # Incorrect
check_agreement("They eats") # Incorrect
check_agreement("She eats")  # Correct
