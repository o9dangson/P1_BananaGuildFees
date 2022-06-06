import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="projectone.cdcrdkperkzv.us-east-2.rds.amazonaws.com",
        database="postgres",
        user="postgres",
        password="wUDjFseC3TpqVCK"
    )

    return conn
