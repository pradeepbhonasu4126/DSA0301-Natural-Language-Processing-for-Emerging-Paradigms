from collections import defaultdict, Counter

# Sample training data: list of (word, tag) pairs
training_data = [
    ("I", "PRON"), ("like", "VERB"), ("cats", "NOUN"),
    ("You", "PRON"), ("like", "VERB"), ("dogs", "NOUN"),
    ("He", "PRON"), ("hates", "VERB"), ("cats", "NOUN"),
    ("Dogs", "NOUN"), ("are", "VERB"), ("friendly", "ADJ"),
]

# Step 1: Count occurrences of each (word, tag)
word_tag_counts = defaultdict(Counter)
tag_counts = Counter()

for word, tag in training_data:
    word_tag_counts[word][tag] += 1
    tag_counts[tag] += 1

# Step 2: Calculate P(tag|word) ~ freq(word, tag) / freq(word)
# We'll store the most probable tag for each word
most_likely_tag = {}

for word, tag_counter in word_tag_counts.items():
    most_common_tag = tag_counter.most_common(1)[0][0]
    most_likely_tag[word] = most_common_tag

# Step 3: Tagging function using the most likely tag for known words,
# and a default tag "NOUN" for unknown words
def tag_sentence(sentence):
    tokens = sentence.split()
    tagged = []
    for token in tokens:
        tag = most_likely_tag.get(token, "NOUN")  # default to NOUN if unknown
        tagged.append((token, tag))
    return tagged

# Example usage
test_sentence = "I hate dogs"
tagged_sentence = tag_sentence(test_sentence)
print(tagged_sentence)
