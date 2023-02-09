import psycopg2

host = ''
port = ''
database = ''
username = ''
password = ''

def connect_to_insert(request_id):
    insert = f'''INSERT INTO some_table
(request_id, org_info, address, email, is_final, activity_form_brief)
VALUES({request_id}, 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "Релиз близко!"', '100001 САТУРН ПЛАНЕТА АСТЕРОИДНЫЙ ПОЯС НЕМЕЗИДА, КОСМИЧЕСКАЯ СТАНЦИЯ АТЛАНТИС, ДОК №5', 'reliz_blizko@mail.com', false, NULL);'''

    try:
        connectus = psycopg2.connect(dbname=database,
                                     user=username,
                                     password=password,
                                     host=host,
                                     port=port)
        cursor = connectus.cursor()
        cursor.execute(insert)
        connectus.commit()
        count = cursor.rowcount
        print(f"{count} rows inserted")
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с бд:", error)
    finally:
        cursor.close()
        connectus.close()

if __name__ == "__main__":
    connect_to_insert(request_id)
