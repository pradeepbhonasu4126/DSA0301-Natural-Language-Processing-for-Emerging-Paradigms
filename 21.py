import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

def extract_noun_phrases_with_meaning(sentence):
    doc = nlp(sentence)
    results = []
    for np in doc.noun_chunks:
        results.append((np.text, f"This is likely a noun phrase: '{np.text}'"))
    return results

# Example usage
sentence = "The quick brown fox jumps over the lazy dog."
results = extract_noun_phrases_with_meaning(sentence)

print("Noun Phrases and Semantic Hints:")
for np, meaning in results:
    print(f"- {np} → {meaning}")
