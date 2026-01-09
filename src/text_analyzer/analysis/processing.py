import string
from collections import Counter
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords, wordnet


# Download necessary NLTK data
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('stopwords')

# Initialize Lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def clean_text(text: str) -> list[str]:
    """Remove punctuation, lowercase, and remove stopwords."""
    translator = str.maketrans("", "", string.punctuation)
    clean = text.translate(translator)
    return [word.lower() for word in clean.split() if word.lower() not in stop_words]

def get_wordnet_pos(treebank_tag: str):
    """Map NLTK POS tag to WordNet POS tag."""
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def lemmatize_words(words: list[str]) -> list[str]:
    """Lemmatize words using POS-aware tagging."""
    pos_tags = nltk.pos_tag(words)
    return [lemmatizer.lemmatize(word, get_wordnet_pos(pos)) for word, pos in pos_tags]

def generate_ngrams(words: list[str], n: int) -> list[tuple[str]]:
    """Generate n-grams from a list of words."""
    return [tuple(words[i:i+n]) for i in range(len(words)-n+1)]

def count_ngrams(words: list[str], min_freq: int = 2) -> dict[str, dict]:
    """Return filtered unigram, bigram, trigram counts with minimum frequency."""
    unigrams = words
    bigrams = generate_ngrams(words, 2)
    trigrams = generate_ngrams(words, 3)

    unigram_counts = {k: v for k, v in Counter(unigrams).items() if v >= min_freq}
    bigram_counts = {k: v for k, v in Counter(bigrams).items() if v >= min_freq}
    trigram_counts = {k: v for k, v in Counter(trigrams).items() if v >= min_freq}

    return {
        "unigrams": unigram_counts,
        "bigrams": bigram_counts,
        "trigrams": trigram_counts
    }
