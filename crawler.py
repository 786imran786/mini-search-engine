import requests
from bs4 import BeautifulSoup
from collections import deque
import time
from urllib.parse import urljoin
import sqlite3 

conn=sqlite3.connect("search_engine.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    title TEXT,
    content TEXT
)
""")

conn.commit()

#data stucture creation
queue = deque()
visited = set()

start_url="https://www.realpython.com"

queue.append(start_url)
Max_page=300 #s define how many pages should crawler visit
def normalize_url(url):
    return url.rstrip("/")

while queue:
    url = normalize_url(queue.popleft())
    if len(visited)>=Max_page:
        break
    if url in visited:
        continue
    visited.add(url)
    try:
        response=requests.get(url,timeout=5)#timeout make sure that no infinite waiting for the request
        time.sleep(1) # used because its bad behaviour to send request without delay
        html=response.text
        soup=BeautifulSoup(html,"html.parser") 
        title = soup.title.string if soup.title else "No Title"
        paragrapghs = soup.find_all("p")
        headings = soup.find_all(["h1", "h2", "h3"])
        content=""
        for h in headings:
            content += h.get_text().strip() + " " # get text remove html tags store in it
        for p in paragrapghs:
            content += p.get_text().strip() + " " # get text remove html tags store in it
        cursor.execute("""
            INSERT INTO pages (url, title, content)
            VALUES (?, ?, ?)
            """, (url, title, content))
        conn.commit()
        print("=============================================Saved to database===========================================")
        links=soup.find_all("a")
        for link in links:
            href = normalize_url(urljoin(url, link.get("href")))
            if href and href.startswith("http"):
                if href not in visited: #checking if url is not already visited 
                    if "realpython.com" in href:
                        queue.append(href)
    except Exception as e:
        print("exception ",e)
        print("for this url:-",url)      


