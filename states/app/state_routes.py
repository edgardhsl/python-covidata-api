# -*- coding: utf-8 -*-

# -----------------------------------------------------------
# NewsAPI - v1.0
# Módulo para buscar notícias do NewsAPI.org
#
# 2021 Edgard H. Santos Lopes, Bahia, Brasil
# email edgardhwp@outlook.com
# -----------------------------------------------------------


from pathlib import Path
import json
from flask import request, Response, jsonify, Blueprint

stateRoutes = Blueprint('states', __name__)

@stateRoutes.route("/", methods=["GET"])
def states():
    
    dbDir = str(Path().absolute()) + '/db/states.json'
    states = json.load(open(dbDir))

    return states;


