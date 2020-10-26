# -*- coding: utf-8 -*-

__author__ = "Francisco Granados"
__copyright__ = "FrankjMinor 2020, Personal Project"
__version__ = "t0.0.1"
__maintainer__ = "Francisco Granados"
__email__ = "franciscominor19@outlook.com"
__status__ = "Develop"

# standar library 
from http import HTTPStatus
import sys

# flask library
from flask import jsonify
from flask import request
from flask import Flask

# services local library
from Services.DivisasService import BmxDivisas

# model local library
from Models.BigQueryModel import BigQueryData

# config local library
from Config.cfn import headers
from Config.cfn import headers

def handler(request):

    if request.method == 'OPTIONS':
        return ('', HTTPStatus.NO_CONTENT, headers)

    
    json_data = request.get_json()
    
    if request.method == 'GET':
        args =request.args

        #function to get data
        response = BmxDivisas(requeriment=args).get_data()
        return (jsonify(response),HTTPStatus.OK)