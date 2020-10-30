#!/usr/bin/env python3
"""
obfuscated text
"""

import re
import logging
from typing import List


def logger():
    """
    setup logger
    :return: logger instance
    """
    a_logger = logging.getLogger(__name__)
    a_logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
    file_handler = logging.FileHandler('filtered_logger.log')
    file_handler.setFormatter(formatter)

    a_logger.addHandler(file_handler)
    return a_logger


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
    a_log = logger()
    # spl_msg = message.split(separator)

    # GOT "name=egg;email=eggmin@eggsample.com;password=eggcellent;
    # date_of_birth=12/12/1986;"

    # EXP name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;

    for field in fields:
        message = re.sub(rf'(?<={field}=).*?(?={separator})', redaction,
                         message)
    a_log.info(message)
    return message
