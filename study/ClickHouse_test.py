import csv
import sys
from pprint import pprint
from clickhouse_driver import Client

class Click:
    def __init__(self, db_set):
        self.host, self.database, self.username, self.password = db_set

    def _connect_database(self):
        connectus = Client(self.host,
                    database=self.database,
                    user=self.username,
                    password=self.password)
        return connectus

    def query(self, select):
        try:
            connectus = self._connect_database()
            print("Execute")
            fetch = connectus.execute(select, with_column_types=True)
            print(fetch)
            print("Keep calm. Execute successful")
            return fetch
        except Exception as ex:
            print("Panic:\nException:\n", ex)
            raise SystemExit

    @staticmethod
    def to_table(coll_names: list, data: dict, save: bool = False):
        table = [dict(zip(coll_names, row)) for row in data]
        if save:
            with open('file.csv', 'w', newline='') as output_file:
                dict_writer = csv.DictWriter(output_file, coll_names)
                dict_writer.writeheader()
                dict_writer.writerows(table)
        return table

def main():
    host = ''
    bd = ''
    user = ''
    pswd = ''

    db_set = [host,
              bd,
              user,
              pswd]

    select = f'''SELECT COUNT(*), toDate(dt) as date,
                FROM something
                WHERE toYear(dt) = '2021' AND
                (toString(toMonth(dt)) IN ('6', '7', '8'))
                GROUP BY date, toMonth(dt)'''
    click = Click(db_set)
    reply, coll_types = click.query(select)
    table = click.to_table([tuple[0] for tuple in coll_types], reply, save=True)
    pprint(table)

if __name__ == '__main__':
    main()
