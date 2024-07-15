import logging
from paho.mqtt import client as mqtt_client


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class MQTT:
    def __init__(self, client_id: str, broker_address: str, broker_port: int, topic_prefix: str):
        self.client_id = client_id
        self.broker_address = broker_address
        self.broker_port = broker_port
        self.topic_prefix = topic_prefix
        self.message_handler = None
        self.client = self.connect()

    def connect(self):
        client = mqtt_client.Client(self.client_id)
        client.on_connect = self.on_connect
        client.connect(self.broker_address, self.broker_port)
        return client

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            log.info("Connected to MQTT broker.")
        else:
            log.error(f"Failed to connect, code {rc}")

    def subscribe(self, topic: str = "#", callback = None):
        self.message_handler = callback
        self.client.on_message = self.on_message
        self.client.subscribe(self.topic_prefix + topic)

    def on_message(self, client, userdata, msg):
        topic = msg.topic[len(self.topic_prefix):]
        message = msg.payload.decode()
        if self.message_handler:
            self.message_handler(topic, message)
        else:
            log.info(f"{topic} = {message}")

    def run(self):
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()

    def publish(self, topic, data):
        result, _ = self.client.publish(self.topic_prefix + topic, data)
        if result != 0:
            log.warn(f"Failed to send message!")

