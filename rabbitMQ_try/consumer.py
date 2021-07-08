#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()


def callback(ch, method, properties, body):
    print(f'[x] Received {body}')


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True
)
print(f'[x] Waiting for message to exit press ctrl + C')
channel.start_consuming()
