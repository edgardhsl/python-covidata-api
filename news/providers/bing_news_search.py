# -*- coding: utf-8 -*-

# -----------------------------------------------------------
# NewsAPI - v1.0
# Módulo para buscar notícias do Rapid News Search (Bing)
#
# 2021 Edgard H. Santos Lopes, Bahia, Brasil
# email edgardhwp@outlook.com
# -----------------------------------------------------------

import sys, os
import requests
import json
import base64
from flask import make_response, jsonify

sys.path.append(os.getcwd())

from factories.news_result import NewsResult

class BingNewsSearch:
    __url          = '';
    __urlNewsApi   = 'https://bing-news-search1.p.rapidapi.com/news/search'
    __apiKey       = ''
    __lang         = 'pt-BR'
    __keywords     = ''

    __page: int    = 1
    __size: int    = 10

    __response     = {};
    
    __imageFault   = 'https://s.itl.cat/pngfile/s/136-1361462_computer-hacker-cyber-crime-latest-news-animated-wallpaper.png';

    def __mountApi(self):
        self.__url = self.__urlNewsApi+'?q=('+self.__keywords+')&mkt='+self.__lang+'&rapidapi-key='+self.__apiKey
        return self.__url;

    def apiToken(self, token):
        self.__apiKey = token

    def page(self, pageNumber):
        self.__page = pageNumber

    def keywords(self, keywords):
        separator = ' OR '
        self. __keywords = separator.join(keywords)
        
    def size(self, pageSize):
        self.__size = pageSize
                
    def request(self):
        self.__mountApi();
        finalUrl = self.__url + '&count='+str(self.__size)+'&offset='+str(((int(self.__page) - 1) * int(self.__size)))+'&originalImg=true'
        print(finalUrl)
        self.__response = requests.get(finalUrl).text
        return self.__response
    
    def parse(self):
        response = json.loads(self.__response);
        
        if(response.get('message')):
           return make_response(jsonify({'code': 500, 'message': response.get('message')}), 500)

        results = list(map(self.mapResults, response.get('value')));
        return make_response(jsonify({'code': 200, 'total': len(results), 'results': results}), 200)
    
    def mapResults(self, item):
        return NewsResult(
            item.get('name'),
            item.get('description'),
            item.get('image').get('contentUrl') if item.get('image') else self.__imageFault,
            item.get('provider')[0].get('name'),
            item.get('url')
        ).toJSON()


