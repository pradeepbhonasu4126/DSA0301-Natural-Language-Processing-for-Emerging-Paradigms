import spacy

# Load the pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

# Input text for NER
text = "Vietnam is a Southeast Asian country known for its beaches, rivers, Buddhist pagodas and bustling cities."

# Process the text
doc = nlp(text)

# Output the entities and their labels
for entity in doc.ents:
    print(f"Entity: {entity.text}, Label: {entity.label_}")
