from collections import Counter

def print_top_ngrams(ngram_counts: dict, n: int = 10, min_freq: int = 2):
    """
    Print the top n n-grams from a count dictionary.

    Args:
        ngram_counts: Dictionary of n-gram counts.
        n: Number of top items to print.
        min_freq: Minimum frequency threshold (for display purposes).
    """
    ngram_type = "unigram" if all(isinstance(k, str) for k in ngram_counts) else f"{len(next(iter(ngram_counts), []))}-gram"
    print(f"\nTop {ngram_type}s (freq >= {min_freq}):")
    for k, count in Counter(ngram_counts).most_common(n):
        # join tuples for bigrams/trigrams, leave unigrams as-is
        if isinstance(k, tuple):
            k_display = ' '.join(k)
        else:
            k_display = k
        print(f"{k_display}: {count}")
