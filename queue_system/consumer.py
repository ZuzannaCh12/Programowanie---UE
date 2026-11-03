import csv
import os
import sys
import time

QUEUE_FILE = os.path.join(os.path.dirname(__file__), "queue.csv")
WORK_DURATION = 30


def process_queue(consumer_id: str) -> None:
    print(f"[Consumer {consumer_id}] Uruchomiono. Oczekiwanie na zadania...")

    while True:
        if not os.path.exists(QUEUE_FILE):
            time.sleep(5)
            continue

        rows = []
        job_to_do = None

        with open(QUEUE_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            for row in reader:
                if row:
                    rows.append(row)

        for row in rows:
            if row[1] == "pending":
                job_to_do = row
                row[1] = "in_progress"
                break

        if job_to_do:
            with open(QUEUE_FILE, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                if headers:
                    writer.writerow(headers)
                writer.writerows(rows)

            job_id = job_to_do[0]
            print(f"[Consumer {consumer_id}] Rozpoczęto zadanie {job_id} (30s)...")
            time.sleep(WORK_DURATION)

            with open(QUEUE_FILE, "r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                headers = next(reader, None)
                current_rows = [r for r in reader if r]

            for row in current_rows:
                if row[0] == job_id:
                    row[1] = "done"
                    break

            with open(QUEUE_FILE, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                if headers:
                    writer.writerow(headers)
                writer.writerows(current_rows)

            print(f"[Consumer {consumer_id}] Zakończono zadanie {job_id}.")
        else:
            time.sleep(5)


if __name__ == "__main__":
    c_id = sys.argv[1] if len(sys.argv) > 1 else "1"
    process_queue(c_id)