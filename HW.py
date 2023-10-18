import psycopg2

def create_db(conn):
    conn.execute('''
                CREATE TABLE IF  NOT EXISTS client(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(40) NOT NULL,
                    surname VARCHAR(60) NOT NULL,
                    email TEXT NOT NULL
                );
                ''')
    conn.execute('''
                CREATE TABLE IF  NOT EXISTS phones(
                    id SERIAL PRIMARY KEY,
                    client_id integer references Client(id),
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

def change_client(conn, client_id, first_name, last_name, email, phones):
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
    if first_name:
        conn.execute('''
                    SELECT name FROM client
                    WHERE name like first_name;
                    ''')
    elif last_name:
        conn.execute('''
                    SELECT surname FROM client
                    WHERE surname like last_name;
                    ''')
    elif email:
        conn.execute('''
                    SELECT email FROM client
                    WHERE email like email;
                    ''')
    elif phone:
        conn.execute('''
                    SELECT number FROM phones
                    WHERE number like phone;
                    ''')
    else:
        None

with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
    pass
conn.close()

if __name__ == "__main__":
    print(create_db())