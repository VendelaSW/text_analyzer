from text_analyzer.io.file_reader import select_file, read_text
from text_analyzer.analysis.processing import TextAnalyzer
from text_analyzer.output.output import print_top_ngrams
from text_analyzer.utils.logger import log, debug, warning

def run():
    """
    Main workflow for the Text Analyzer.
    Select a file, process text, and print top n-grams.
    """
    # Step 1: Let the user pick a file
    file_path = select_file()
    if not file_path:
        log("No file selected. Exiting.")
        return
    log(f"Selected file: {file_path}")

    # Step 2: Read the text
    text = read_text(file_path)
    log(f"Text length: {len(text)} characters")

    # Step 3: Process text
    analyzer = TextAnalyzer(text)

    # Step 4: Output results

    print_top_ngrams(analyzer.ngram_counts["unigrams"])

    print_top_ngrams(analyzer.ngram_counts["bigrams"])

    print_top_ngrams(analyzer.ngram_counts["trigrams"])

    log("Run complete")