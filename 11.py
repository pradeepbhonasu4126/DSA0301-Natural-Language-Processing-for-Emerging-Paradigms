import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser

# Define a new grammar
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N | 'He' | 'She' | 'They'
VP -> V NP | V
Det -> 'a' | 'the' | 'A' | 'The'
N -> 'dog' | 'cat'
V -> 'chases' | 'runs'
""")

# Create the parser
parser = RecursiveDescentParser(grammar)

# Define the sentence to parse
sentence = "The cat chases a dog".split()  # Use original sentence

# Parse the sentence and print the resulting tree
for tree in parser.parse(sentence):
    tree.pretty_print()
