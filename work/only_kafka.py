import time
import json
import confluent_kafka as ck
from sys import argv

def send_json(topic):
    #srv = 'gitlab-ci.ru:9092' # sand_bootstrap_servers
    srv = 'server:9092' # test_bootstrap_servers
    client = ''

    proconf = {'bootstrap.servers': srv, 'client.id': client}
    producer = ck.Producer(proconf)
    with open('tmp_for_kafka', 'r') as fd:
        for line in fd:
            line = line.rstrip('\n')
            json.dumps(line)
            print(line)
            producer.produce(topic, value=line)
            producer.flush()
            #time.sleep(5)

if __name__ == '__main__':
    send_json(argv[1])
