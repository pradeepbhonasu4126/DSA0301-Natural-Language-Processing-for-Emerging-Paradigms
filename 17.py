from nltk.corpus import wordnet as wn

# Example 1: Get Synsets of the word "dog"
synsets_dog = wn.synsets("dog")
print("Synsets for 'dog':")
for synset in synsets_dog:
    print(f"{synset.name()}: {synset.definition()}")

print("\n")

# Example 2: Get Synsets of the word "bank"
synsets_bank = wn.synsets("bank")
print("Synsets for 'bank':")
for synset in synsets_bank:
    print(f"{synset.name()}: {synset.definition()}")

print("\n")

# Example 3: Get Synonyms for "happy"
synsets_happy = wn.synsets("happy")
print("Synonyms for 'happy':")
for synset in synsets_happy:
    for lemma in synset.lemmas():
        print(f"{lemma.name()}")

print("\n")

# Example 4: Find hypernyms (broader concepts) for "dog"
hypernyms_dog = synsets_dog[0].hypernyms()
print("Hypernyms (broader concepts) for 'dog':")
for hypernym in hypernyms_dog:
    print(hypernym.name())

print("\n")

# Example 5: Find hyponyms (specific concepts) for "dog"
hyponyms_dog = synsets_dog[0].hyponyms()
print("Hyponyms (specific concepts) for 'dog':")
for hyponym in hyponyms_dog:
    print(hyponym.name())
