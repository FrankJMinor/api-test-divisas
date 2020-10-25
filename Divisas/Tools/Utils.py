# -*- coding: utf-8 -*-

# local source
from Errors.IncorrectRequest import TypeOfValue


class ValidateValues(object):
    """
    Validate Request 
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Validate type of value in fields from json request to proccess the Payment Totalplay Pay Fintech

        Attributes:
            data (Dict):Input paylod for the API Payment Fintech

        Raises:
            TypeOfValue: Describe incorrect type value from some field in request
    """
    def __init__(self, data):
        #use regex
        array = [
            {
                'field': 'anio',
                'type': 0,
                'value': data['anio']
            },
            {
                'field': 'meses',
                'type': 'string',
                'value': data['meses']
            }
        ]

        self.validate_fields(array)


    def validate_fields(self, paylod):
        for item in paylod:
            if isinstance(item['value'], type(item['type'])):
                None
            else:
                self.validate_raise(item['value'], item['field'], type(item['type']))

    def validate_raise(self, value, field, type):
        raise TypeOfValue(value, field, type)
