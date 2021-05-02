# -*- coding: utf-8 -*-

# -----------------------------------------------------------
# NewsAPI - v1.0
# Módulo para buscar notícias do NewsAPI.org
#
# 2021 Edgard H. Santos Lopes, Bahia, Brasil
# email edgardhwp@outlook.com
# -----------------------------------------------------------

import requests
import json
from flask import jsonify, Response
class CoviDataAPI:
    
    __url          = 'https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod/PortalEstado';
    __response     = {}

    def filterById(self, _id):
        result   = json.loads(self.__response)
        filtered = {}
        for state in result:
            if state['_id'] == _id:
                filtered = state
                
        return Response(json.dumps(filtered), status=200, mimetype='application/json')

    def response(self):
        return self.__response;

    def request(self):
        self.__response = requests.get(self.__url).text
        return self;
    
    def parse(self):
        return Response(self.__response, status=200, mimetype='application/json')


