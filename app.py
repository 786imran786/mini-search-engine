from flask import Flask
from flask import render_template
from flask import request

from search_engine import search

app = Flask(__name__)

# -----------------------------------
# SIMPLE SEARCH CACHE
# -----------------------------------

cache = {}

# -----------------------------------
# SEARCH HISTORY
# -----------------------------------

search_history = []

# -----------------------------------
# HOME ROUTE
# -----------------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    query = ""

    results = []

    suggestions = []

    page = request.args.get("page", 1, type=int)

    per_page = 5

    if request.method == "POST":

        query = request.form["query"].strip()

        # SAVE SEARCH HISTORY
        if query:

            search_history.append(query)

        # -----------------------------
        # CACHE CHECK
        # -----------------------------

        if query in cache:

            results = cache[query]

        else:

            results = search(query)

            cache[query] = results

        # -----------------------------
        # QUERY SUGGESTIONS
        # -----------------------------

        for old_query in search_history:

            if (
                query.lower() in old_query.lower()
                and old_query != query
            ):

                suggestions.append(old_query)

        # REMOVE DUPLICATES
        suggestions = list(set(suggestions))

    # -----------------------------------
    # PAGINATION
    # -----------------------------------

    total_results = len(results)

    total_pages = (
        total_results + per_page - 1
    ) // per_page

    start = (page - 1) * per_page

    end = start + per_page

    paginated_results = results[start:end]

    # -----------------------------------
    # RETURN TEMPLATE
    # -----------------------------------

    return render_template(

        "index.html",

        query=query,

        results=paginated_results,

        suggestions=suggestions,

        page=page,

        total_pages=total_pages,

        history=search_history[-5:]
    )

# -----------------------------------
# RUN APP
# -----------------------------------

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )