#!/usr/bin/env python3
"""
obfuscated text
"""

import re
import logging
from typing import List, ByteString
import mysql.connector
import os

PII_FIELDS: List[str] = ['name', 'email', 'phone', 'ssn', 'password']


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    returns obfuscated text
    :param fields: a list of strings representing all fields to obfuscate
    :param redaction: a string representing by what the field will be obfuscated
    :param message: a string representing the log line
    :param separator: a string representing by which character is 
    separating all fields in the log line
    :return: obfuscated text
    """
    # GOT "name=egg;email=eggmin@eggsample.com;password=eggcellent;
    # date_of_birth=12/12/1986;"

    # EXP name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
    for field in fields:
        message = re.sub(rf'(?<={field}=).*?(?={separator})', redaction,
                         message)
    return message


def get_logger() -> logging.Logger:
    """
    creates the logger object
    :return: loggin.logger object
    """
    user_data_logger = logging.getLogger('user_data')
    user_data_logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    user_data_logger.addHandler(stream_handler)

    return user_data_logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    setup the mysql connector

    :return:
    """

    db_connection = mysql.connector.Connect(
        host=os.getenv('PERSONAL_DATA_DB_HOST'),
        user=os.getenv('PERSONAL_DATA_DB_USERNAME'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD'),
        database=os.getenv('PERSONAL_DATA_DB_NAME')
    )
    return db_connection


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        init
        :param fields: list of fields to obfuscate
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        giving format to the record
        :param record: the record instance
        :return: formatted record message
        """

        obfuscated = filter_datum(self.fields, self.REDACTION, record.msg,
                                  self.SEPARATOR)
        record.msg = obfuscated
        return super(RedactingFormatter, self).format(record)


def main() -> None:
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute('SELECT * FROM users')

    # get users
    users = cursor.fetchall()

    logger = get_logger()

    for user in users:
        msg = ''
        for key, value in user.items():
            msg += f'{key}={value};'
        logger.info(msg)


if __name__ == '__main__':
    main()

# PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=Java_1988 PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./filtered_logger.py
