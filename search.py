import sqlite3
conn = sqlite3.connect("search_engine.db")

cursor = conn.cursor()

query = input("Enter what yoiyu want to search:-")


cursor.execute("""

SELECT title, url

FROM pages

WHERE content LIKE ?

""", ("%" + query + "%",))

results = cursor.fetchall()
if not results:
    print("No results found.")

for result in results:

    print("\nTITLE:", result[0])

    print("URL:", result[1])