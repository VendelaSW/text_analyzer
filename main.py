from io.file_reader import select_file, read_text
from analysis.processing import clean_text, lemmatize_words, count_ngrams
from output.output import print_top_ngrams

def run():
    """
    Main workflow for the Text Analyzer.
    Select a file, process text, and print top n-grams.
    """
    # Step 1: Let the user pick a file
    file_path = select_file()
    if not file_path:
        print("No file selected. Exiting.")
        return

    # Step 2: Read the text
    text = read_text(file_path)

    # Step 3: Process text
    words = clean_text(text)
    lemmas = lemmatize_words(words)
    ngram_counts = count_ngrams(lemmas)

    # Step 4: Output results
    print_top_ngrams(ngram_counts["unigrams"])
    print_top_ngrams(ngram_counts["bigrams"])
    print_top_ngrams(ngram_counts["trigrams"])
