import json
import uuid
from kafka import KafkaConsumer, KafkaProducer, TopicPartition

class Kafkin:
    def __init__(self, srv, grp1, topic1, grp2, topic2):
        self.consumer = KafkaConsumer(
            topic1,
            group_id=grp1,
            bootstrap_servers=srv,
            auto_offset_reset='earliest',
            enable_auto_commit=False,
            value_deserializer=lambda m: json.loads(m.decode())
        )
        self.consumer_end = KafkaConsumer(
            group_id=grp1,
            bootstrap_servers=srv,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda m: json.loads(m.decode())
        )
        self.topic1 = topic1
        self.producer = KafkaProducer(
            bootstrap_servers=srv
        )
        self.topic2 = topic2
        self.group_id = grp2

    def get_all(self):
        print(f"Connected to bootstrap: {self.consumer.bootstrap_connected()}")
        for message in self.consumer:
            print(f"{message.topic}:{message.offset}:{message.value}")

    def get_one(self, latest=None):
        if latest is None:
            latest = 1
        print(f"Connected to bootstrap: {self.consumer_end.bootstrap_connected()}")
        # Получить список всех партиций
        partitions_for_topic = self.consumer_end.partitions_for_topic(self.topic1)
        # Перебрать все партиции если их несколько
        if partitions_for_topic:
            partitions = []
        # Добавить их в список
            for partition in partitions_for_topic:
                partitions.append(TopicPartition(self.topic1, partition))
        # Найти у них конечные оффсеты
        end_offsets = self.consumer_end.end_offsets(partitions)
        # Назначить их текущему консьюмеру
        self.consumer_end.assign([*end_offsets])
        # Перебрать все партиции и вычислить последний
        for key_partition, value_end_offset in end_offsets.items():
            new_calculated_offset = value_end_offset - latest
            new_offset = new_calculated_offset if new_calculated_offset >= 0 else 0
        self.consumer_end.seek(key_partition, new_offset)
        counter = 0
        messages = []
        for message in self.consumer_end:
            print(message.value)
            counter += 1
            messages.append(json.dumps(message.value))
            if counter == latest:
                break
        print("end")
        print(*messages, sep='\n')
        return messages

    def put_one(self, message: str):
        try:
            self.producer.send(self.topic2, value=message.encode())
            self.producer.flush()
            return 0
        except Exception as ex:
            return ex

    def migrate(self, num: int):
        messages = self.get_one(num)
        for message in messages:
            self.put_one(message)
            print(type(message))

def main():
    topic1 = "test_topic1"
    topic2 = "test_topic2"
    grp1 = str(uuid.uuid1())
    grp2 = str(uuid.uuid1())
    srv = ["something-ci.ru:9092"]
    consumer = Kafkin(srv, grp1, topic1, grp2, topic2)
    #consumer.get_one()
    #topic1 = "test_topic2"
    #consumer.get_all()
    #message = '{"awesome":2294,"docType":"anybody","id":6332342,"date":"2022-11-14"}'
    #consumer.put_one(message)
    #consumer.migrate(5)

if __name__ == '__main__':
    main()
