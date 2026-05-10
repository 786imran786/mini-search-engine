import sqlite3
import re
import math
from nltk.stem import PorterStemmer

# STOPWORDS
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

# STEMMER
stemmer = PorterStemmer()

def search(query):

    # DATABASE CONNECTION
    conn = sqlite3.connect("search_engine.db")

    cursor = conn.cursor()

    # FETCH PAGES
    cursor.execute(
        "SELECT id, title, url, content FROM pages"
    )

    pages = cursor.fetchall()

    # DOCUMENT FREQUENCY
    document_frequency = {}

    total_documents = len(pages)

    # BUILD DOCUMENT FREQUENCY
    for page in pages:

        content = page[3]

        words = [

            stemmer.stem(word)

            for word in re.findall(
                r'\w+',
                content.lower()
            )

            if word not in stopwords
        ]

        unique_words = set(words)

        for word in unique_words:

            if word not in document_frequency:
                document_frequency[word] = 0

            document_frequency[word] += 1

    # QUERY PROCESSING
    query_words = [

        stemmer.stem(word)

        for word in re.findall(
            r'\w+',
            query.lower()
        )

        if word not in stopwords
    ]

    page_scores = {}

    # MAIN SEARCH
    for page in pages:

        page_id = page[0]

        title = page[1]

        url = page[2]

        content = page[3]

        words = [

            stemmer.stem(word)

            for word in re.findall(
                r'\w+',
                content.lower()
            )

            if word not in stopwords
        ]

        word_counts = {}

        for word in words:

            if word not in word_counts:
                word_counts[word] = 0

            word_counts[word] += 1

        score = 0

        for query_word in query_words:

            if query_word in word_counts:

                tf = (
                    word_counts[query_word]
                    / len(words)
                )

                idf = math.log(
                    total_documents /
                    document_frequency[query_word]
                )

                score += tf * idf

        if score > 0:

            page_scores[page_id] = {

                "title": title,

                "url": url,

                "score": round(score, 5),

                "snippet": content[:250]
            }

    # SORT RESULTS
    ranked_results = sorted(

        page_scores.values(),

        key=lambda x: x["score"],

        reverse=True
    )

    return ranked_results