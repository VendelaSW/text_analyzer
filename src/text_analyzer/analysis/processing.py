import string
from collections import Counter
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords, wordnet
from text_analyzer.utils.logger import log, debug, warning

# Download necessary NLTK data
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('stopwords')

class TextAnalyzer:
    def __init__(self, text: str, min_freq: int = 2):
        self.raw_text = text
        self.min_freq = min_freq
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

        # Process text
        self.words = self._clean_text(text)
        self.lemmatized_words = self._lemmatize_words(self.words)
        self.ngram_counts = self._count_ngrams(self.lemmatized_words)

        log(f"TextAnalyzer: {len(self.words)} words, {len(self.lemmatized_words)} lemmas processed")
        log(f"TextAnalyzer: {len(self.ngram_counts['unigrams'])} unigrams, "
            f"{len(self.ngram_counts['bigrams'])} bigrams, "
            f"{len(self.ngram_counts['trigrams'])} trigrams counted")

    def _clean_text(self, text: str) -> list[str]:
        """Remove punctuation, lowercase, and remove stopwords."""
        translator = str.maketrans("", "", string.punctuation)
        clean = text.translate(translator)
        return [word.lower() for word in clean.split() if word.lower() not in self.stop_words]

    def _get_wordnet_pos(self, treebank_tag: str):
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

    def _lemmatize_words(self, words: list[str]) -> list[str]:
        """Lemmatize words using POS-aware tagging."""
        pos_tags = nltk.pos_tag(words)
        return [self.lemmatizer.lemmatize(word, self._get_wordnet_pos(pos)) for word, pos in pos_tags]

    def _generate_ngrams(self, words: list[str], n: int) -> list[tuple[str]]:
        """Generate n-grams from a list of words."""
        return [tuple(words[i:i+n]) for i in range(len(words)-n+1)]

    def _count_ngrams(self, words: list[str]) -> dict[str, dict]:
        """Return filtered unigram, bigram, trigram counts with minimum frequency."""
        unigrams = words
        bigrams = self._generate_ngrams(words, 2)
        trigrams = self._generate_ngrams(words, 3)

        unigram_counts = {k: v for k, v in Counter(unigrams).items() if v >= self.min_freq}
        bigram_counts = {k: v for k, v in Counter(bigrams).items() if v >= self.min_freq}
        trigram_counts = {k: v for k, v in Counter(trigrams).items() if v >= self.min_freq}

        return {
            "unigrams": unigram_counts,
            "bigrams": bigram_counts,
            "trigrams": trigram_counts
        }
