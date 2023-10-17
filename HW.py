import psycopg2

def create_db(conn):
    conn.execute('''
                CREATE TABLE IF  NOT EXISTS client(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(40) NOT NULL,
                    surname VARCHAR(60) NOT NULL,
                    email TEXT NOT NULL,
                    number INTEGER
                );
                ''')

def add_client(conn, first_name, last_name, email, phones=None):
    conn.execute('''
                INSERT INTO clients(name, surname, email, number)
                VALUES(first_name, last_name, email, phones);                  
                ''')

def add_phone(conn, client_id, phone):
    conn.execute('''
                INSERT INTO clients(client_id, number)
                VALUES(client_id, phone);
                ''')

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    conn.execute('''
                UPDATE client
                SET name = first_name, surname = last_name, email = email, number = phones
                WHERE id = client_id;
                ''')

def delete_phone(conn, client_id, phone):
    conn.execute('''
                DELETE FROM clients(number)
                WHERE id = client_id;
                ''')

def delete_client(conn, client_id):
    conn.execute('''
                DELETE FROM clients;
                ''')

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    conn.execute('''
                SELECT name, surname, email, number FROM client
                WHERE name like first_name, surname like last_name, email like email, number like phone;
                ''')


with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
    print(create_db())

conn.close()
