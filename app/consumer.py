from kafka import KafkaConsumer
import click
TODO_TOPIC = "topic-test"

class Consumer():
    def __init__(self) -> None:
        self.consumer = KafkaConsumer(TODO_TOPIC, bootstrap_servers="kafka:29092")

    def consume(self):
        self.consumer.subscribe([TODO_TOPIC])
        for msg in self.consumer:
            click.echo(f"Consuming message {msg}")
