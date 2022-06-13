#request

from flask import request
import psycopg2
from database.connection import get_connection
from database.request_dto import Request

#create
def insert_user_request(user_id, amount, desc):
    conn = get_connection()
    cur = conn.cursor()

    insert_q = f"INSERT INTO request_table VALUES(default, {user_id}, {amount}, '{desc}', default) RETURNING request_id"

    try:
        cur.execute(insert_q)
        request_id = cur.fetchone()[0]
        conn.commit()
        if (request_id is not None):
            return request_id
        else:
            return 0
    except(psycopg2.DatabaseError) as err:
        print(err)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()
            
#read for Users
def select_all_req_by_user_id(user_id):
    conn = get_connection()
    cur = conn.cursor()

    qry = f"SELECT * FROM request_table WHERE user_id={user_id};"

    try:
        cur.execute(qry)
        list_of_reqs = []
        while True:
            record = cur.fetchone()
            if record is None:
                break
            else:
                list_of_reqs.append(Request(record[0], record[1], record[2], record[3], record[4]))
        if len(list_of_reqs) > 0:
            return list_of_reqs
        else:
            return None
            
    except(psycopg2.DatabaseError) as err:
        print(err)
        return None
    finally:
        if conn is not None:
            conn.close()

#read for Managers
def select_all_req_by_manager_id(user_id):
    conn = get_connection()
    cur = conn.cursor()

    qry = f"SELECT * FROM request_table WHERE NOT user_id={user_id} AND status='Pending';"

    try:
        cur.execute(qry)
        list_of_req = []
        while True:
            record = cur.fetchone()
            if record == None:
                break
            else:
                list_of_req.append( Request(record[0], record[1], record[2], record[3], record[4]) )
        if len(list_of_req) > 0:
            return list_of_req
        else:
            return None
    except(psycopg2.DatabaseError) as err:
        print(err)
        return None
    finally:
        if conn is not None:
            conn.close()

#update
def update_req_by_req_id(req_id, var_Name, value):
    conn = get_connection()
    cur = conn.cursor()

    qry = f"UPDATE request_table SET {var_Name}='{value}' WHERE request_id={req_id};"

    try:
        cur.execute(qry)
        conn.commit()
        return True
    except(psycopg2.DatabaseError) as err:
        print(err)
        conn.rollback()
        return False
    finally:
        if conn is not None:
            conn.close()
            
#delete
def remove_req_by_req_id(req_id):
    conn = get_connection()
    cur = conn.cursor()

    qry = f"DELETE FROM request_table WHERE request_id = {req_id};"
    try:
        cur.execute(qry)
        conn.commit()
        return True
    except(psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
        return False
    finally:
        if conn is not None:
            conn.close()