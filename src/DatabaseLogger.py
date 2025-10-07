import datetime
import json
import subprocess
from pathlib import Path

DB_FILE = Path(__file__).parent / "results_db.json"

class DatabaseLogger:
    def __init__(self):
        self.db_path = DB_FILE

    def log_result(self, test_case_id, quality_score, max_score):
        """Appends a new test result to the JSON log file."""
        # 1. Get current timestamp and commit hash
        timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
        try:
            commit_hash = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).strip().decode('utf-8')
        except (subprocess.CalledProcessError, FileNotFoundError):
            commit_hash = "unknown"

        # 2. Create the new log entry
        new_entry = {
            "timestamp": timestamp,
            "commit_hash": commit_hash,
            "test_case_id": test_case_id,
            "quality_score": quality_score,
            "max_score": max_score
        }

        # 3. Read the existing data, append, and write back
        try:
            with open(self.db_path, 'r') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(new_entry)

        with open(self.db_path, 'w') as f:
            json.dump(data, f, indent=2)


    def load_results(self):
        try:
            with open(self.db_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
