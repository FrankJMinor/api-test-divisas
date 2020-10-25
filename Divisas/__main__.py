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

def handler(request):
    
    json_data = request.get_json()
    
    if request.method == 'GET':
        args =request.args

        #function to get data
        response = BmxDivisas(requeriment=args).get_data()
        return (jsonify(response),200)

        

## NO SE MANEJA EN CLOUD
if __name__ == '__main__':
    from flask import Flask, request
    app = Flask(__name__)

    # option 1
    @app.route('/Divisas', methods=['GET', 'OPTIONS'])
    def test():
        return handler(request)
    app.run(host='0.0.0.0', port=5002, debug=False)