import requests
from .utils_text import generate_prefix_suffix_variants

class YouTubeAutocompleteScraper:
    API_URL = "https://suggestqueries.google.com/complete/search"

    def _fetch(self, query: str, language: str, country: str):
        params = {
            "client": "firefox",
            "ds": "yt",
            "q": query,
            "hl": language,
            "gl": country
        }
        try:
            response = requests.get(self.API_URL, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            return data[1] if len(data) > 1 else []
        except Exception as e:
            print(f"[ERROR] Failed fetching autocomplete for '{query}': {e}")
            return []

    def get_suggestions(self, base_query: str, language="en", country="US",
                        use_prefix=False, use_suffix=False):
        queries = [base_query]

        if use_prefix or use_suffix:
            variants = generate_prefix_suffix_variants(base_query, use_prefix, use_suffix)
            queries.extend(variants)

        all_suggestions = set()
        for q in queries:
            suggestions = self._fetch(q, language, country)
            for s in suggestions:
                all_suggestions.add(s)

        return sorted(all_suggestions)