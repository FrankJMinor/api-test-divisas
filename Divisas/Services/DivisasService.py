# -*- coding: utf-8 -*-

__all__ = ['BmxDivisas']

# gallery local library
from Gallery import graph as gh

# models local library
from Models.BigQueryModel import BigQueryData

# utilities local library
from Utilities.data import gen_json

# tools local library
from Tools.Utils import ValidateValues

from Errors.IncorrectRequest import body_error

class BmxDivisas():

    gh.init_graph()

    def __init__(self,requeriment):
        self.requirement = requeriment
        super().__init__()

    def get_data(self):

        #ValidateValues(self.requirement)

        months = self.requirement['meses'].replace("-", ",")
        year = self.requirement['anio']

        
        data = BigQueryData(year=year, months=months).exec_query()

        #In case the query doesn't get results, it returns empty array
        if len(data) == 0:
            return []

        response = {}
        message = gen_json(data)
        response['grafico'] = gh.grafico
        response['message'] = message
        return response