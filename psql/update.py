import psycopg2
from sys import argv

host = ''
port = ''
database = ''
username = ''
password = ''

def connect_to_update(request_id):
    update = f'''UPDATE some_table
                SET status = 42
                WHERE request_id = {request_id}
                AND code_id IN (1, 3, 5, 8, 42)'''
    try:
        connectus = psycopg2.connect(dbname=database,
                                     user=username,
                                     password=password,
                                     host=host,
                                     port=port)
        cursor = connectus.cursor()
        cursor.execute(update)
        connectus.commit()
        count = cursor.rowcount
        print(f"{count} rows updated")
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с бд:", error)
    finally:
        cursor.close()
        connectus.close()

if __name__ == "__main__":
    connect_to_update(argv[1])
