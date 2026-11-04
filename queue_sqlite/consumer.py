import sys
import time
from queue_sqlite.database import get_connection, init_db

WORK_DURATION = 30


def process_queue(consumer_id: str) -> None:
    init_db()
    print(f"[Consumer {consumer_id}] Uruchomiono (SQLite). Oczekiwanie na zadania...")

    while True:
        job_id = None

        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute(
                "SELECT id FROM jobs WHERE status = 'pending' ORDER BY created_at ASC LIMIT 1"
            )
            row = cursor.fetchone()

            if row:
                job_id = row["id"]

                cursor.execute(
                    "UPDATE jobs SET status = 'in_progress' WHERE id = ?",
                    (job_id,),
                )
                conn.commit()

        if job_id:
            print(f"[Consumer {consumer_id}] Rozpoczęto zadanie {job_id} (30s)...")
            time.sleep(WORK_DURATION)

            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE jobs SET status = 'done' WHERE id = ?",
                    (job_id,),
                )
                conn.commit()

            print(f"[Consumer {consumer_id}] Zakończono zadanie {job_id}.")
        else:
            time.sleep(5)


if __name__ == "__main__":
    c_id = sys.argv[1] if len(sys.argv) > 1 else "1"
    process_queue(c_id)