import nltk
from nltk.parse.earleychart import EarleyChartParser
from nltk import CFG

# Define a more complex grammar
grammar = CFG.fromstring("""
S -> NP VP
NP -> 'He' | 'She' | 'They' | Det N
VP -> V | V NP
V -> 'runs' | 'run'
Det -> 'a' | 'the'
N -> 'dog' | 'cat'
""")

# Create an Earley Chart parser with the grammar
parser = EarleyChartParser(grammar)

# Define the sentence to parse
sentence = "She runs a dog".split()

# Parse the sentence and print the resulting tree
for tree in parser.parse(sentence):
    tree.pretty_print()
