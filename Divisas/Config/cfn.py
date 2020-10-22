# -*- coding: utf-8 -*-

headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, GET, PUT, DELETE,OPTIONS' ,
        'Access-Control-Allow-Headers': 'content-type, accept, x-custom-header, Authorization',
        'Access-Control-Max-Age': '3600'
    }

#token SIE API BM
toekn = 'c94ad844a798f3fc61abda40814a83949c4fa2a588a278ff2d96dca127149a32'

url = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/:idSerie/datos/:fechaIni/:fechaFin"

udis = 'SP68257'
dollar = 'SF63528'