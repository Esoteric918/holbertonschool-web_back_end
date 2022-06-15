#!/usr/bin/env python3
'''Write a function called filter_datum that
    returns the log message obfuscated:
'''


import re


def filter_datum(fields, redaction, message, separator):
    '''
    fields: list of strings representing all fields to obfuscate
    redaction: string representing by what the field will be obfuscated
    message: string representing the log line
    separator: string representing by which character is separating all
    fields in the log line (message)
    return: string representing the log line obfuscated
    '''
    for string in fields:
        regex = fr"(?<={string}=).*?(?={separator})"
        message = re.sub(r'{}'.format(regex), redaction, message)
    return message
