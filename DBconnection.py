import psycopg2 as pg

try:
    conn = pg.connect(
        host="localhost",
        database="ass2",
        port=5432,
        user="postgres",
        password="1337"
    )
    cursor = conn.cursor()
    print("Connection established")
    cursor.execute("SELECT VERSION();")
    print(cursor.fetchone())

except Exception as err:
    print("Something went wrong...")
    print(err)


def get_tables(curs):
    curs.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    return curs.fetchone()


def get_schema(table, curs):
    curs.execute(f"SELECT table_name, column_name, data_type FROM information_schema.columns WHERE table_name = 'public.{table}'")
    return curs.fetchall()


def display_content(table, curs):
    curs.execute(f"SELECT * FROM {table}")
    contents = curs.fetchall()
    for c in contents:
        print(c)


def create_row(table, curs):
    pass


def change_row(table, curs):
    pass


def delete_row(table, curs):
    pass


def load_json(table, json_file, curs):
    pass


display_content('offers', cursor)