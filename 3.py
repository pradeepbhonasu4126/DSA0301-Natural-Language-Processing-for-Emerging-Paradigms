import nltk
from nltk.stem import PorterStemmer, LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Download required NLTK data files (only need to run once)
nltk.download('wordnet')
nltk.download('omw-1.4')  # for WordNet lemmatizer improvements

# Sample words
words = ['running', 'runs', 'ran', 'easily', 'fairly', 'better']

# Initialize stemmers and lemmatizer
porter = PorterStemmer()
lancaster = LancasterStemmer()
lemmatizer = WordNetLemmatizer()

print("Word\tPorterStemmer\tLancasterStemmer\tLemmatizer (verb)")

for word in words:
    # Perform stemming
    porter_stem = porter.stem(word)
    lancaster_stem = lancaster.stem(word)
    # Lemmatize with POS = verb (default is noun)
    lemma = lemmatizer.lemmatize(word, pos='v')
    print(f"{word}\t{porter_stem}\t\t{lancaster_stem}\t\t\t{lemma}")
