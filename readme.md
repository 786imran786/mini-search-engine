# 🔎 Mini Search Engine

A full-stack intelligent search engine built using **Python, Flask, SQLite, NLP, and TF-IDF ranking**.  
This project crawls webpages, processes textual data using NLP techniques, indexes documents efficiently, and retrieves ranked search results through a responsive web interface.

---

# 🚀 Features

## 🌐 Web Crawling
- BFS-based web crawler
- Domain-restricted crawling
- Duplicate URL prevention
- URL normalization
- Polite crawling using delays
- HTML parsing using BeautifulSoup
- Content extraction and storage

## 🧠 NLP Processing
- Tokenization
- Stopword removal
- Porter stemming using NLTK
- Query preprocessing

## 📊 Search Engine Logic
- Inverted indexing
- TF-IDF ranking
- Relevance-based retrieval
- Ranked search results
- Snippet generation

## ⚡ Backend Features
- Flask backend
- SQLite database integration
- Search history tracking
- Query suggestions
- Pagination support
- Lightweight caching system

## 🎨 Frontend
- Modern responsive UI
- Dark-themed interface
- Search bar with result cards
- Clickable URLs
- Search snippets

---

# 🏗️ Project Workflow

```text
Crawler
   ↓
Web Scraping
   ↓
SQLite Database
   ↓
Tokenization
   ↓
Stopword Removal
   ↓
Stemming
   ↓
TF-IDF Ranking
   ↓
Flask Backend
   ↓
Search Engine UI
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core programming |
| Flask | Backend framework |
| SQLite | Database |
| BeautifulSoup | HTML parsing |
| Requests | HTTP requests |
| NLTK | NLP preprocessing |
| HTML/CSS | Frontend development |
| TF-IDF | Ranking algorithm |

---

# 📂 Project Structure

```text
mini_search_engine/
│
├── app.py
├── crawler.py
├── search_engine.py
├── indexer.py
├── search_engine.db
├── requirements.txt
├── README.md
│
├── templates/
│     └── index.html
│
└── static/
      └── style.css
```

---

# ⚙️ Installation

## 1️⃣ Clone The Repository

```bash
git clone YOUR_REPOSITORY_LINK
cd mini_search_engine
```

---

## 2️⃣ Create Virtual Environment (Optional)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running The Project

## Step 1 — Crawl Webpages

```bash
python crawler.py
```

This step:
- Visits webpages
- Extracts content
- Cleans and processes data
- Stores documents into SQLite database

---

## Step 2 — Start Flask Server

```bash
python app.py
```

---

## Step 3 — Open Browser

```text
http://127.0.0.1:5000
```

---

# 🔍 Example Search Queries

```text
python programming
machine learning
binary tree
dynamic programming
graph algorithms
data science
```

---

# 🌟 Future Improvements

- Async crawling
- PageRank implementation
- Trie-based autocomplete
- AI semantic search
- Transformer embeddings
- Elasticsearch integration
- PostgreSQL support
- MongoDB support
- User authentication system

---

# 🚀 Deployment

This project can be deployed easily on:

- Railway
- Render
- Koyeb
- Oracle Cloud

---

# 📌 Resume Description

Developed and deployed a full-stack intelligent search engine using Flask, SQLite, NLP preprocessing, TF-IDF ranking, and web crawling techniques. Implemented indexing, ranked retrieval, query preprocessing, pagination, caching, and responsive frontend rendering for efficient information retrieval.

---

# 👨‍💻 Author

**Md Imran Siddiqui**  
B.Tech Computer Science Student

---
