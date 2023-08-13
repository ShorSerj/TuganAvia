import db

# --- SELECT

@db.connection_for_sqlite
def get_users(cursor):

    query = """SELECT * FROM users"""

    cursor.execute(query)
    result = cursor.fetchall()

    return result


@db.connection_for_sqlite
def auth_user(cursor, user_type, values):

    query = f"""SELECT id FROM {user_type}s WHERE email = ? AND password = ?"""

    cursor.execute(query, values)
    result = cursor.fetchall()

    return result
# --- INSERT


@db.connection_for_sqlite
def registration(cursor, user_type, values):

    query = f"""INSERT INTO {user_type}s (email, password) VALUES (?, ?) RETURNING id"""

    cursor.execute(query, values)
    result = cursor.fetchone()

    result = result[0]

    return result

# --- UPDATE


@db.connection_for_sqlite
def update_profile(cursor, user_type, values):

    query = f"""UPDATE {user_type}s SET phone = ?, first_name = ?, last_name = ? WHERE id = ?"""
    cursor.execute(query, values)


# --- DELETE


# --- CREATE

@db.connection_for_sqlite
def create_registration_users(cursor):

    query = """CREATE TABLE "users" (
id INTEGER PRIMARY KEY,
first_name TEXT,
last_name TEXT,
email TEXT NOT NULL UNIQUE,
phone TEXT,
registered TEXT DEFAULT CURRENT_TIMESTAMP
);"""

    cursor.execute(query)


if __name__ == '__main__':
    #values = ('i', 'i', 'wwws@gmail.com', 'phone')
    #registration_user(values)
    #create_registration_users()

    result = get_users()
    print(result)