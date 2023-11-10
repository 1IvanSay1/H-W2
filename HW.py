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

def change_client(conn, client_id, **kwargs):
    for key, value in kwargs.items():
        conn.execute(f'''
                     UPDATE client
                     SET {key} = {value}
                     WHERE id = client_id;
                     ''')

def delete_phone(conn, client_id, phone):
    conn.execute('''
                DELETE FROM clients(number)
                WHERE id = client_id;
                ''')

def delete_client(conn, client_id):
    conn.execute('''
                DELETE FROM phones
                WHERE client_id = client_id;
                ''')
    conn.execute('''
                DELETE FROM clients
                WHERE id = client_id;
                ''')

def find_client(conn, **kwargs):
    for key, value in kwargs.items():
        conn.execute(f'''
                     SELECT {key} FROM client
                     WHERE {key} like {value};
                     ''')

with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
    pass
conn.close()

if __name__ == "__main__":
    print(create_db())