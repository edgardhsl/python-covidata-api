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
from flask import request, Blueprint
from providers.covidata import CoviDataAPI

covidataRoutes = Blueprint('covidata', __name__)
coviDataApi = CoviDataAPI();

@covidataRoutes.route("/", methods=["GET"])
def covidata():
    request = coviDataApi.request()

    return request.parse();

@covidataRoutes.route("/<_id>", methods=["GET"])
def covidataById(_id):
    request = coviDataApi.request()
    return request.filterById(_id);



