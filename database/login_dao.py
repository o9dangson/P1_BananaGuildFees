import psycopg2
from database.connection import get_connection

def select_user_by_login(username, password):
    conn = get_connection()
    cur = conn.cursor()

    read_q = f"SELECT user_id FROM user_login WHERE username='{username}' AND password='{password}'"

    try:
        cur.execute(read_q)
        user_id = cur.fetchone()
        if (user_id is not None):
            return user_id[0]
        else:
            return 0
    except(psycopg2.DatabaseError) as err:
        print(err)
        return 0
    finally:
        if conn is not None:
            conn.close()