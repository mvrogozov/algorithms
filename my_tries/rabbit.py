import pika
import os
import sys


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


def main():
    credentials = pika.PlainCredentials(
        'adminuser',
        'user1'
    )
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            'localhost',
            5672,
            '/vhost1',
            credentials=credentials
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_consume(
        queue='hello',
        auto_ack=True,
        on_message_callback=callback
    )
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
