import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

# Define a Probabilistic Context-Free Grammar (PCFG)
grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'He' [0.3] | 'She' [0.7]
VP -> V NP [0.5] | V Adv [0.5]
V -> 'runs' [0.6] | 'run' [0.4]
Adv -> 'quickly' [1.0]
""")

# Create a Viterbi parser
parser = ViterbiParser(grammar)

# Define a sentence to parse
sentence = "She runs quickly".split()

# Parse the sentence and print the best parse tree
for tree in parser.parse(sentence):
    tree.pretty_print()
