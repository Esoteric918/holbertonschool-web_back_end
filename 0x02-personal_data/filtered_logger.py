#!/usr/bin/env python3
'''Write a function called filter_datum that
    returns the log message obfuscated:
'''

import re
import logging


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list):
        ''' Initialize the formatter with the fields to redact'''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields


    def format(self, record: logging.LogRecord) -> str:
        ''' Format the log message '''
        msg = super().format(record)
        logList =  (filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR))
        return logList.replace(";", "; ")
        NotImplementedError

def filter_datum(fields, redaction, message, separator):
    '''
    fields: list of strings representing all fields to obfuscate
    redaction: string representing by what the field will be obfuscated
    message: string representing the log line
    separator: string representing by which character is separating all
    fields in the log line (message)
    return: string representing the log line obfuscated
    '''
    for fields in fields:
        regex = fr"(?<={fields}=).*?(?={separator})"
        message = re.sub(r'{}'.format(regex), redaction, message)
    return message

def get_logger() -> logging.Logger:
    '''
    return: logger object
    '''

    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    formatter = RedactingFormatter(PII_FIELDS)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.propagate = False
    logger.addHandler(handler)
    return logger

