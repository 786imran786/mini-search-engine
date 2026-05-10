import sqlite3
import re
import math

# DATABASE CONNECTION
conn = sqlite3.connect("search_engine.db")
cursor = conn.cursor()

# FETCH ALL PAGES
cursor.execute("SELECT id, content FROM pages")

pages = cursor.fetchall()

# INVERTED INDEX
# Structure:
# {
#   word: [page_ids]
# }

inverted_index = {}

# DOCUMENT FREQUENCY
# Structure:
# {
#   word: number_of_documents_containing_word
# }

document_frequency = {}

# TF-IDF INDEX
# Structure:
# {
#   word: {
#       page_id: tfidf_score
#   }
# }

tfidf_index = {}

# TOTAL DOCUMENTS
total_documents = len(pages)

# -----------------------------
# STEP 1: BUILD INVERTED INDEX
# -----------------------------

for page in pages:
    page_id = page[0]
    content = page[1]
    # TOKENIZATION
    words = re.findall(r'\w+', content.lower())
    # BUILD INVERTED INDEX
    for word in words:
        if word not in inverted_index:
            inverted_index[word] = []
        if page_id not in inverted_index[word]:
            inverted_index[word].append(page_id)
    # DOCUMENT FREQUENCY
    unique_words = set(words)
    for word in unique_words:
        if word not in document_frequency:
            document_frequency[word] = 0
        document_frequency[word] += 1

# -----------------------------
# STEP 2: CALCULATE TF-IDF
# -----------------------------

for page in pages:
    page_id = page[0]
    content = page[1]
    words = re.findall(r'\w+', content.lower())
    # WORD COUNT INSIDE DOCUMENT
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1
    # CALCULATE TF-IDF
    for word, count in word_counts.items():
        # TERM FREQUENCY
        tf = count / len(words)
        # INVERSE DOCUMENT FREQUENCY
        idf = math.log(total_documents / document_frequency[word])
        # FINAL SCORE
        score = tf * idf
        # STORE SCORE
        if word not in tfidf_index:
            tfidf_index[word] = {}
        tfidf_index[word][page_id] = score

# -----------------------------
# PRINT INVERTED INDEX
# -----------------------------

print("\n========== INVERTED INDEX ==========\n")

for word, page_ids in list(inverted_index.items())[:20]:
    print(word, "→", page_ids)

# -----------------------------
# PRINT TF-IDF SCORES
# -----------------------------

print("\n========== TF-IDF SCORES ==========\n")

for word, page_scores in list(tfidf_index.items())[:20]:
    print("\nWORD:", word)
    for page_id, score in page_scores.items():
        print("PAGE:", page_id, " SCORE:", round(score, 5))