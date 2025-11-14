import json

class JSONExporter:
    @staticmethod
    def export(data, file_path: str):
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"[INFO] JSON exported to {file_path}")
        except Exception as e:
            print(f"[ERROR] Failed writing JSON: {e}")