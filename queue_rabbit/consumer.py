import json
import sys
import time
import pika

RABBIT_HOST = "localhost"
RABBIT_PORT = 8081
QUEUE_NAME = "tasks_queue"
WORK_DURATION = 30  # Czas trwania pracy w sekundach


def process_queue(consumer_id: str) -> None:
    credentials = pika.PlainCredentials("guest", "guest")
    parameters = pika.ConnectionParameters(
        host=RABBIT_HOST,
        port=RABBIT_PORT,
        credentials=credentials,
        heartbeat=600,
    )
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    channel.basic_qos(prefetch_count=1)

    def callback(ch, method, properties, body) -> None:
        data = json.loads(body.decode("utf-8"))
        job_id = data.get("id")

        data["status"] = "in_progress"
        print(
            f"[Consumer {consumer_id}] Pobrano {job_id} "
            f"(status: {data['status']}). Praca 30s..."
        )

        time.sleep(WORK_DURATION)

        data["status"] = "done"
        print(
            f"[Consumer {consumer_id}] Zakończono {job_id} "
            f"(status: {data['status']})."
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)

    print(f"[Consumer {consumer_id}] Uruchomiono (RabbitMQ). Oczekiwanie...")
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print(f"\n[Consumer {consumer_id}] Zatrzymano.")
        connection.close()


if __name__ == "__main__":
    c_id = sys.argv[1] if len(sys.argv) > 1 else "1"
    process_queue(c_id)