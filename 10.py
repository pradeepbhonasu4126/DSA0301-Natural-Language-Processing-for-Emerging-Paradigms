# Sample sentence (tokenized)
sentence = ["I", "can", "fish"]

# Step 1: Initial tagging: tag every word as NOUN by default
tags = ["NN"] * len(sentence)

print("Initial tags:", list(zip(sentence, tags)))

# Step 2: Define a transformation rule:
# If the current word is 'can' and previous tag is PRON, tag 'can' as a modal verb 'MD'
def apply_transformation_rule(words, tags):
    for i in range(len(words)):
        if words[i].lower() == 'can':
            # Check previous tag
            if i > 0 and tags[i-1] == 'PRON':
                tags[i] = 'MD'  # modal verb
    return tags

# Step 3: Before applying rule, let's fix the pronoun 'I'
# We hardcode 'I' as PRON
for i, word in enumerate(sentence):
    if word.lower() == 'i':
        tags[i] = 'PRON'

print("Tags before transformation:", list(zip(sentence, tags)))

# Step 4: Apply transformation rule
tags = apply_transformation_rule(sentence, tags)

print("Tags after transformation:", list(zip(sentence, tags)))
