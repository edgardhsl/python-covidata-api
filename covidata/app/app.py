# -*- coding: utf-8 -*-

# -----------------------------------------------------------
# NewsAPI - v1.0
# Módulo para buscar notícias do NewsAPI.org
#
# 2021 Edgard H. Santos Lopes, Bahia, Brasil
# email edgardhwp@outlook.com
# -----------------------------------------------------------
from flask import Flask
app = Flask("States");

from covidata_routes import covidataRoutes
app.register_blueprint(covidataRoutes, url_prefix='/api/covidata')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)