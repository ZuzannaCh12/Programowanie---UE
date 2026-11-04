import sys
import time
import uuid
from queue_sqlite.database import get_connection, init_db


def add_job(count: int = 1) -> None:
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        for _ in range(count):
            job_id = str(uuid.uuid4())[:8]
            created_at = time.strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute(
                "INSERT INTO jobs (id, status, created_at) VALUES (?, ?, ?)",
                (job_id, "pending", created_at),
            )
            print(f"[Producer] Dodano zadanie do SQLite: {job_id}")
        conn.commit()


if __name__ == "__main__":
    count_to_add = 100 if "--100" in sys.argv else 1
    add_job(count_to_add)