# -*- coding: utf-8 -*-

# -----------------------------------------------------------
# NewsAPI - v1.0
# Módulo para buscar notícias do NewsAPI.org
#
# 2021 Edgard H. Santos Lopes, Bahia, Brasil
# email edgardhwp@outlook.com
# -----------------------------------------------------------

import sys, os
sys.path.append(os.getcwd())

import json
from flask import request, Response, jsonify, Blueprint

from providers.bing_news_search import BingNewsSearch

searchNewsApi = BingNewsSearch()
searchNewsApi.apiToken('0747618d13msh47b9af5664213a8p1cfd8bjsnf92b6e4c179d')

newsRoutes = Blueprint('news', __name__)

@newsRoutes.route("/", methods=["GET"])
def news():
    page = request.args.get('page');
    size = request.args.get('size');

    if(page is not None):
        searchNewsApi.page(page)

    if(size is not None):
        searchNewsApi.size(size)

    # Palarvras chaves para retornarem nas notícias
    searchNewsApi.keywords(['covid', 'corona', 'ministério da saúde', 'vacina', 'coronavac', 'pfizer', 'vacina oxford', 'sputnik v'])

    res = searchNewsApi.request();

    return searchNewsApi.parse()


