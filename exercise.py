# use the news api and the requests module to fetch the daily news related todifferent topics 
# go to https:/newsapi.org/ and explore the various options to build your own application

import requests

API_KEY = "307d1d18fc4e4b4dae6de8fb94a06dc2"
BASE_URL = "https://newsapi.org/v2/top-headlines"

def fetch_news_by_category(category="general", country="us", limit=5):
    """
    Fetches news headlines based on category (e.g., technology, sports, business).
    """
    params = {
        "apiKey": API_KEY,
        "category": category,
        "country": country,
        "pageSize": limit
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raises an HTTPError if status code is not 200
        data = response.json()
        
        if data.get("status") == "ok":
            articles = data.get("articles", [])
            print(f"\n--- Top {len(articles)} Headlines in [{category.upper()}] ---")
            for index, article in enumerate(articles, start=1):
                title = article.get("title", "No Title")
                source = article.get("source", {}).get("name", "Unknown Source")
                url = article.get("url", "#")
                
                print(f"\n{index}. {title}")
                print(f"   Source: {source}")
                print(f"   Link: {url}")
        else:
            print(f"Error from API: {data.get('message', 'Unknown error')}")
            
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")

def search_news_by_keyword(query, limit=5):
    """
    Searches articles matching a specific keyword or phrase.
    """
    search_url = "https://newsapi.org/v2/everything"
    params = {
        "apiKey": API_KEY,
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": limit
    }
    
    try:
        response = requests.get(search_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data.get("status") == "ok":
            articles = data.get("articles", [])
            print(f"\n--- Top {len(articles)} Search Results for '{query}' ---")
            for index, article in enumerate(articles, start=1):
                print(f"\n{index}. {article.get('title')}")
                print(f"   Source: {article.get('source', {}).get('name')}")
                print(f"   Link: {article.get('url')}")
        else:
            print(f"Error from API: {data.get('message')}")
            
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")

# --- Example Usage ---
if __name__ == "__main__":
    # 1. Get Top Headlines in Technology
    fetch_news_by_category(category="technology", limit=3)
    
    # 2. Get Top Headlines in Sports
    fetch_news_by_category(category="sports", limit=3)

    # 3. Search for a custom keyword across all news
    search_news_by_keyword(query="Artificial Intelligence", limit=3)