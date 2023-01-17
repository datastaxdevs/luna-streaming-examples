#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(port=5672))
channel = connection.channel()

try:
    channel.queue_declare("test-queue")
    print("created test-queue queue")

    channel.basic_publish(exchange="", routing_key="test-queue", body="test".encode('utf-8'))
    print("published message test")

    _, _, res = channel.basic_get(queue="test-queue", auto_ack=True)
    assert res is not None, "should have received a message"
    print("received message: " + res.decode())

    channel.queue_delete("test-queue")
    print("deleted test-queue queue")

finally:
    connection.close()