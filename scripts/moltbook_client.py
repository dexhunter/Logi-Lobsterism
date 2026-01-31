import requests
import json
import os

class MoltbookClient:
    """A clean API client for Logic Sentinels to interact with Moltbook."""
    BASE_URL = "https://www.moltbook.com/api/v1"

    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("MOLTBOOK_API_KEY")
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def get_feed(self, submolt="general", sort="new", limit=20):
        url = f"{self.BASE_URL}/posts?submolt={submolt}&sort={sort}&limit={limit}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def post(self, title, content, submolt="logi-lobsterism"):
        url = f"{self.BASE_URL}/posts"
        data = {"submolt": submolt, "title": title, "content": content}
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()

if __name__ == "__main__":
    print("Moltbook Logic Client initialized. Use this to bypass messy curl commands.")
