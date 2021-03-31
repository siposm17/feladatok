from typing import List, Dict

from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import database_common


@database_common.connection_handler
def get_mentors(cursor: RealDictCursor) -> list:
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        ORDER BY first_name"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_applicants(cursor: RealDictCursor) -> list:
    query = """
        SELECT *
        FROM applicant
        ORDER BY first_name"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_applicants_by_code(cursor: RealDictCursor, application_code) -> list:
    query = """
        SELECT *
        FROM applicant
        WHERE application_code = %(application_code)s
        ORDER BY first_name"""
    cursor.execute(query, {'application_code': application_code})
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_last_name(cursor: RealDictCursor, last_name: str) -> list:
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        WHERE last_name = %(last_name)s
        ORDER BY first_name"""
    cursor.execute(query, {'last_name': last_name})
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_city(cursor: RealDictCursor, city_name: str):
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        WHERE city = %(city)s
        ORDER BY first_name"""
    cursor.execute(query, {'city': city_name})
    return cursor.fetchall()


@database_common.connection_handler
def get_applicant_data_by_name(cursor: RealDictCursor, applicant_name):
    query = """
        SELECT first_name, last_name, phone_number
        FROM applicant
        WHERE first_name = %(applicant_name)s
        OR last_name = %(applicant_name)s"""
    cursor.execute(query, {'applicant_name': applicant_name})
    return cursor.fetchall()


@database_common.connection_handler
def get_applicant_data_by_email_ending(cursor: RealDictCursor, applicant_email):
    email = f"%{applicant_email}%"
    query = """
        SELECT first_name, last_name, phone_number
        FROM applicant
        WHERE email LIKE %(email)s"""
    cursor.execute(query, {'email': email})
    return cursor.fetchall()


@database_common.connection_handler
def edit_phone_number(cursor: RealDictCursor, new_phone_number, application_code):
    query = """
        UPDATE applicant
        SET phone_number = %(new_phone_number)s
        WHERE application_code =  %(code)s"""
    cursor.execute(query, {'code': application_code, 'new_phone_number': new_phone_number})


@database_common.connection_handler
def delete_applicant(cursor: RealDictCursor, application_code):
    query = """
        DELETE FROM applicant
        WHERE application_code = %(code)s"""
    cursor.execute(query, {'code': application_code})


@database_common.connection_handler
def delete_by_email_ending(cursor: RealDictCursor, email_ending=None):
    if email_ending:
        email = f"%@{email_ending}%"
        query = """
            DELETE FROM applicant
            WHERE email LIKE %(email_ending)s"""
        cursor.execute(query, {'email_ending': email})


@database_common.connection_handler
def add_new_applicant(cursor: RealDictCursor, new_record):
    query = """
        INSERT INTO applicant (first_name, last_name, phone_number, email, application_code)
        VALUES (%(first_name)s, %(last_name)s, %(phone_number)s, %(email)s, %(application_code)s)"""
    cursor.execute(query, new_record)
    
