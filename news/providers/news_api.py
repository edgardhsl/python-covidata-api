# -*- coding: utf-8 -*-

# -----------------------------------------------------------
# NewsAPI - v1.0
# Módulo para buscar notícias do NewsAPI.org
#
# 2021 Edgard H. Santos Lopes, Bahia, Brasil
# email edgardhwp@outlook.com
# -----------------------------------------------------------

import requests

class NewsAPI:
    __url          = '';
    __urlNewsApi   = 'https://newsapi.org/v2/everything'
    __apiKey       = ''
    __lang         = 'pt'
    __keywords     = ''

    __page         = 1
    __size         = 10

    def __mountApi(self):
        self.__url = self.__urlNewsApi+'?q=('+self.__keywords+')&language='+self.__lang+'&apiKey='+self.__apiKey
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
        finalUrl = self.__url + '&pageSize='+str(self.__size)+'&page='+str(self.__page)
        return requests.get(finalUrl).text