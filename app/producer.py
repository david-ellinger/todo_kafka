from kafka import KafkaProducer
import click

class Producer():

    def __init__(self) -> None:
        self.producer = KafkaProducer(bootstrap_servers='kafka:29092')

    def produce(self,data:str, topic):
        click.echo("Producing message...")
        self.producer.send(topic, data.encode())
