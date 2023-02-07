import redis
host = ''
password=''

class Monitor():
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        self.connection = None

    def __del__(self):
        try:
            self.reset()
        except:
            pass

    def reset(self):
        if self.connection:
            self.connection_pool.release(self.connection)
            self.connection = None

    def monitor(self):
        if self.connection is None:
            self.connection = self.connection_pool.get_connection(
                'monitor', None)
            print("get_connection")
        self.connection.send_command("monitor")
        return self.listen()

    def parse_response(self):
        return self.connection.read_response()

    def listen(self):
        while True:
            yield self.parse_response()

if  __name__ == '__main__':
    pool = redis.ConnectionPool(host='',
                                port=,
                                db=,
                                password='',
                                decode_responses=True)
    monitor = Monitor(pool)
    commands = monitor.monitor()
    #print(commands)
    #print(monitor.monitor())
