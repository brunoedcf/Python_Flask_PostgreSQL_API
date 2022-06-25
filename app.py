from db_init import CreateDatabase, GetDatabaseConnection
from flask import Flask, request

# CreateDatabase()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def GetUsers():

    try:

        conn = GetDatabaseConnection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM users ORDER BY id ASC;;')
        users = cur.fetchall()
        cur.close()
        conn.close()

        response_data = []

        for user in users:

            response_data.append({
                "id": user[0],
                "name": user[1],
                "pokemons": user[2]
            })
        
        return {
            "status": "Success",
            "data": response_data
        }

    except:

        return {
            "error": "Error"
        }


@app.route('/<id>', methods=['GET'])
def GetUser(id):

    try:

        conn = GetDatabaseConnection()
        cur = conn.cursor()
        query = 'SELECT * FROM users WHERE id =' + f' {id};'
        cur.execute(query)
        user = cur.fetchone() # returns a tuple of the first match
        cur.close()
        conn.close()

        if user == None:
            return {
                "error": "Query Error"
            }

        response_data = {
            "id": user[0],
            "name": user[1],
            "pokemons": user[2]
        }

        return {
            "status": "Success",
            "data": response_data
        }

    except:

        return {
            "error": "Error"
        }


@app.route('/', methods=['POST'])
def AddUser():

    try:

        request_data = request.get_json()

        conn = GetDatabaseConnection()
        cur = conn.cursor()
        query = "INSERT INTO users (name, pokemons) " + f"VALUES (\'{request_data['name']}\', {request_data['pokemons']});"
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()

        return {
            "success": "Success"
        }

    except:

        return {
            "error": "Error"
        }


@app.route('/<id>', methods=['PATCH'])
def UpdateUser(id):

    try:

        request_data = request.get_json()

        conn = GetDatabaseConnection()
        cur = conn.cursor()
        query = f"UPDATE users SET name = '{request_data['name']}', pokemons = {request_data['pokemons']} WHERE id = {id};"
        cur.execute(query)
        conn.commit()
        updated_rows = cur.rowcount
        cur.close()
        conn.close()

        if updated_rows > 0:
            return {
                "success": "Success"
            }
        else:
            return {
            "error": "Query Error"
        }

    except:

        return {
            "error": "Error"
        }


@app.route('/<id>', methods=['DELETE'])
def DeleteUser(id):

    try:

        request_data = request.get_json()

        conn = GetDatabaseConnection()
        cur = conn.cursor()
        query = f"DELETE FROM users WHERE id = {id};"
        cur.execute(query)
        conn.commit()
        updated_rows = cur.rowcount
        cur.close()
        conn.close()

        if updated_rows > 0:
            return {
                "success": "Success"
            }
        else:
            return {
            "error": "Query Error"
        }

    except:

        return {
            "error": "Error"
        }