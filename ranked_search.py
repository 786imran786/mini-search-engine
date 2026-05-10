import sqlite3
import re
import math
from nltk.stem import PorterStemmer

# -----------------------------
# DATABASE CONNECTION
# -----------------------------

conn = sqlite3.connect("search_engine.db")
cursor = conn.cursor()

# -----------------------------
# FETCH ALL PAGES
# -----------------------------

cursor.execute(
    "SELECT id, title, url, content FROM pages"
)

pages = cursor.fetchall()

# -----------------------------
# STOPWORDS
# -----------------------------

stopwords = {
    "the",
    "is",
    "and",
    "of",
    "to",
    "a",
    "in",
    "on",
    "for",
    "with",
    "that",
    "this",
    "it",
    "as",
    "an",
    "are",
    "be",
    "by",
    "from",
    "or",
    "at",
    "was",
    "were"
}

# -----------------------------
# STEMMER
# -----------------------------

stemmer = PorterStemmer()

# -----------------------------
# DOCUMENT FREQUENCY
# -----------------------------

document_frequency = {}

total_documents = len(pages)

# -----------------------------
# BUILD DOCUMENT FREQUENCY
# -----------------------------

for page in pages:

    content = page[3]

    # TOKENIZATION + CLEANING + STEMMING
    words = [

        stemmer.stem(word)

        for word in re.findall(r'\w+', content.lower())

        if word not in stopwords
    ]

    # UNIQUE WORDS ONLY
    unique_words = set(words)

    # DOCUMENT FREQUENCY
    for word in unique_words:

        if word not in document_frequency:
            document_frequency[word] = 0

        document_frequency[word] += 1

# -----------------------------
# USER QUERY
# -----------------------------

query = input("Search: ").lower()

# QUERY TOKENIZATION + CLEANING + STEMMING
query_words = [

    stemmer.stem(word)

    for word in re.findall(r'\w+', query)

    if word not in stopwords
]

# -----------------------------
# PAGE SCORES
# -----------------------------

page_scores = {}

# -----------------------------
# MAIN SEARCH LOGIC
# -----------------------------

for page in pages:

    page_id = page[0]

    title = page[1]

    url = page[2]

    content = page[3]

    # TOKENIZATION + CLEANING + STEMMING
    words = [

        stemmer.stem(word)

        for word in re.findall(r'\w+', content.lower())

        if word not in stopwords
    ]

    # WORD COUNTS
    word_counts = {}

    for word in words:

        if word not in word_counts:
            word_counts[word] = 0

        word_counts[word] += 1

    # PAGE SCORE
    score = 0

    # TF-IDF CALCULATION
    for query_word in query_words:

        if query_word in word_counts:

            # TERM FREQUENCY
            tf = word_counts[query_word] / len(words)

            # INVERSE DOCUMENT FREQUENCY
            idf = math.log(
                total_documents /
                document_frequency[query_word]
            )

            # FINAL SCORE
            score += tf * idf

    page_scores[page_id] = {
        "title": title,
        "url": url,
        "score": score,
        "content": content
    }

# -----------------------------
# SORT RESULTS
# -----------------------------

ranked_results = sorted(

    page_scores.items(),

    key=lambda x: x[1]["score"],

    reverse=True
)

# -----------------------------
# DISPLAY RESULTS
# -----------------------------

print("\n========== SEARCH RESULTS ==========\n")

found = False

for result in ranked_results:

    page_data = result[1]

    if page_data["score"] > 0:

        found = True

        print("TITLE:", page_data["title"])

        print("URL:", page_data["url"])

        print(
            "SCORE:",
            round(page_data["score"], 5)
        )

        # SNIPPET
        snippet = page_data["content"][:250]

        print("SNIPPET:", snippet)

        print("\n" + "-" * 80 + "\n")

# -----------------------------
# NO RESULTS
# -----------------------------

if not found:

    print("No results found.")