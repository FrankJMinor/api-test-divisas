# -*- coding: utf-8 -*-

# standar library
from http import HTTPStatus
import logging
import sys

def body_error(message):
    exc_tuple = sys.exc_info()

    if exc_tuple[1].args:
        http_code = exc_tuple[1].code
    else: 
        http_code = "Error interno en Python" + str(exc_tuple) + " " + str(exc_tuple[1].args)
    error = {}
    detalle = {"@type" : str(exc_tuple[0]), "details" : str(exc_tuple[1].args[0]), 'http_code' : str(http_code)}
    error["error"] = {"developerMessage" : detalle, "message" : message } 
    logging.error(error['error']['message'])
    return error, HTTPStatus.BAD_REQUEST

class TypeOfValue(Exception):
    """Exception raised for value data from Json to the API Divisas

    Atributes:
        value ([type]): [Description]
        message ([type]): [Description]
        response ([type]): [Description]
    """
    def __init__(self, value, message):
        self.value = value
        self.message = message
        self.response = f'Mensaje de errror {message}'
        super().__init__(self.response)

    def __str__(self):
        return self.response