import psycopg2

def CreateDatabase():

    conn = psycopg2.connect(
            host="ec2-34-200-35-222.compute-1.amazonaws.com",
            database="d7imig8o6f9skp",
            user="ybkbucpiubmkvm",
            password="8a16b3277f694b124d9b3c40c63b1feb17b23f5aa71f266c750caff063200b91")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: this creates a new table
    cur.execute('DROP TABLE IF EXISTS users;')
    cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
                                    'name varchar (50) NOT NULL,'
                                    'pokemons integer);'
                                    )

    # Insert data into the table

#     cur.execute('INSERT INTO users (name, pokemons)'
#                 'VALUES (\'Brest\', 5);'
#                 )


#     cur.execute('INSERT INTO users (name, pokemons)'
#                 'VALUES (\'dudaholandah\', 3);'
#                 )

    conn.commit()

    cur.close()

    conn.close()


def GetDatabaseConnection():

    conn = psycopg2.connect(
            host="ec2-34-200-35-222.compute-1.amazonaws.com",
            database="d7imig8o6f9skp",
            user="ybkbucpiubmkvm",
            password="8a16b3277f694b124d9b3c40c63b1feb17b23f5aa71f266c750caff063200b91")

    return conn