import json
import sys
import time
import uuid
import pika

RABBIT_HOST = "localhost"
RABBIT_PORT = 8081
QUEUE_NAME = "tasks_queue"


def get_channel() -> tuple[
    pika.BlockingConnection,
    pika.adapters.blocking_connection.BlockingChannel,
]:
    credentials = pika.PlainCredentials("guest", "guest")
    parameters = pika.ConnectionParameters(
        host=RABBIT_HOST,
        port=RABBIT_PORT,
        credentials=credentials,
    )
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    return connection, channel


def add_job(count: int = 1) -> None:
    connection, channel = get_channel()
    try:
        for _ in range(count):
            job_id = str(uuid.uuid4())[:8]
            payload = {
                "id": job_id,
                "status": "pending",
                "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            }
            channel.basic_publish(
                exchange="",
                routing_key=QUEUE_NAME,
                body=json.dumps(payload),
                properties=pika.BasicProperties(delivery_mode=2),
            )
            print(f"[Producer] Wysłano zadanie do RabbitMQ: {job_id}")
    finally:
        connection.close()


if __name__ == "__main__":
    count_to_add = 100 if "--100" in sys.argv else 1
    add_job(count_to_add)