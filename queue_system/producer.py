import csv
import os
import sys
import time
import uuid

QUEUE_FILE = os.path.join(os.path.dirname(__file__), "queue.csv")


def init_queue_file() -> None:
    if not os.path.exists(QUEUE_FILE):
        with open(QUEUE_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "status", "created_at"])


def add_job(count: int = 1) -> None:
    init_queue_file()
    with open(QUEUE_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for _ in range(count):
            job_id = str(uuid.uuid4())[:8]
            created_at = time.strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([job_id, "pending", created_at])
            print(f"[Producer] Dodano zadanie: {job_id}")


if __name__ == "__main__":
    count_to_add = 100 if "--100" in sys.argv else 1
    add_job(count_to_add)