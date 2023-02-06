from confluent_kafka import Producer
import json
import random
import sh

topic = ''
srvrs = ''
group = ''
client = ''
proconf = {'bootstrap.servers': srvrs, 'client.id': client}
producer = Producer(proconf)

fd = open('json_file')
line = fd.readline()
fd.close()

vibe = json.dumps(line)
print(vibe)
#producer.produce(topic, value=vibe)
#producer.flush() # Synchronous writes
