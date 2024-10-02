import psycopg2
import psycopg2.extras

host = 'localhost'
database = 'test'
user = 'postgres'
password = 'foxboro21'
port_id = '5432'

cur = None
conn = None

try:
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(host=host, database=database, user=user, password=password, port=port_id)

    if conn is not None:
      cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    create_script = ''' CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name varchar(40) NOT NULL,
        age INT NOT NULL,
        greeting varchar(40) NOT NULL
    )''' 

    cur.execute(create_script)

    insert_script = 'INSERT INTO users (id, name, age, greeting) VALUES (%s, %s, %s, %s)'
    insert_values = (1, 'John Doe', 25, 'Hello, World!')
    cur.execute(insert_script, insert_values)

    conn.commit()

except Exception as e:
    print('Connection to database failed: ', e)

finally:
    if cur is not None: cur.close()
    if conn is not None: conn.close()

# So this is where we write out database code
# We need to create a cursor object to interact with the database
# cur = conn.cursor()

# We can execute SQL commands using the cursor object
# cur.execute('SELECT * FROM users')

# We can fetch the results of the query
# result = cur.fetchall()
# print(result)

# We need to commit the transaction
# conn.commit()

# We need to close the cursor
# cur.close()

# We need to close the connection
# conn.close()

