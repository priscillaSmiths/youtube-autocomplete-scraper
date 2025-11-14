import json
import sys
from pathlib import Path
from extractors.youtube_autocomplete import YouTubeAutocompleteScraper
from outputs.exporters import JSONExporter

def load_inputs(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Failed to load input file: {e}")
        sys.exit(1)

def main():
    base_dir = Path(__file__).resolve().parent.parent
    data_file = base_dir / "data" / "inputs.sample.json"

    inputs = load_inputs(str(data_file))

    scraper = YouTubeAutocompleteScraper()

    results = []
    for item in inputs:
        query = item.get("query")
        lang = item.get("language", "en")
        country = item.get("country", "US")
        use_prefix = item.get("use_prefix", False)
        use_suffix = item.get("use_suffix", False)

        print(f"[INFO] Fetching suggestions for '{query}'...")
        suggestions = scraper.get_suggestions(
            query,
            language=lang,
            country=country,
            use_prefix=use_prefix,
            use_suffix=use_suffix,
        )

        results.append({
            "query": query,
            "suggestions": suggestions,
            "language": lang,
            "country": country,
            "use_prefix": use_prefix,
            "use_suffix": use_suffix
        })

    out_file = base_dir / "data" / "sample_output.json"
    JSONExporter.export(results, str(out_file))

    print(f"[INFO] Completed. Results saved to: {out_file}")

if __name__ == "__main__":
    main()