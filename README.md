# Text Analyzer

A simple Python package to analyze text files, demonstrating modular code, classes, logging, and package structure.

## Installation

```bash
# Install in development mode
pip install -e .

# Or normal install
pip install .
```

## Usage

### As a CLI tool
After installation, run from anywhere:
```bash
python -m text_analyzer
```

### As a library
```python
from text_analyzer.processing import TextAnalyzer
from text_analyzer.utils.logger import log

text = "Some example text to analyze."
analyzer = TextAnalyzer(text)
log(f"Top unigrams: {analyzer.ngram_counts['unigrams']}")
```

## Project Structure

```
text_analyzer/                  # Project root
├── .venv/                      # Virtual environment
├── pyproject.toml              # Package configuration
├── README.md                   # This file
└── src/                        # Source directory
    └── Logs/                   # Logs from Logger
    └── text_analyzer/          # Main package
        ├── __init__.py
        ├── __main__.py         # Module entry point
        ├── config.py           # Configuration & path handling
        ├── main.py             # Application workflow
        └── analysis/
            ├── processing.py   # Text processing and TextAnalyzer class
            └── __init__.py
        └── io/
            ├── file_reader.py  # File opener and reader
            └── __init__.py
        └── output/
            ├── output.py       # Output
            └── __init__.py
        └── utils/
            ├── logger.py       # Logger utilities
            └── __init__.py
```

## Key Features

- **TextAnalyzer class**: Cleans, lemmatizes, and generates n-grams from text

- **Logger utility**: Info and debug logging for workflow tracking

- **Config module**: Centralized path handling

- **Modular structure**: Clear separation of concerns for maintainability
