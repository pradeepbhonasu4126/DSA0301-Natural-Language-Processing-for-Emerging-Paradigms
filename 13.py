import nltk
from nltk import CFG

# Define a new grammar for a sentence involving reading actions
grammar = CFG.fromstring("""
S -> NP VP
NP -> 'He' | 'She' | 'They' | Det N
VP -> V | V NP
V -> 'reads' | 'read'
Det -> 'a' | 'the'
N -> 'book' | 'magazine'
""")

# Create the ChartParser with the grammar
parser = nltk.ChartParser(grammar)

# Define the sentence to parse
sentence = "She reads a book"
words = sentence.split()

# Parse the sentence and print the resulting tree
for tree in parser.parse(words):
    tree.pretty_print()
