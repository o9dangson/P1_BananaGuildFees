import psycopg2

from database.connection import get_connection
from database.user_dto import User

def select_user_info_by_user_id(user_id):
    conn = get_connection()
    cur = conn.cursor()

    read_q = f"SELECT * FROM user_info WHERE user_id='{user_id}'"

    try:
        cur.execute(read_q)
        record = cur.fetchone()
        if (record is not None):
            user_info = User(record[0], record[1], record[2], record[3])
            return user_info
        else:
            return None
    except(psycopg2.DatabaseError) as err:
        print(err)
        return None
    finally:
        if conn is not None:
            conn.close()

