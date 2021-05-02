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

from state_routes import stateRoutes
app.register_blueprint(stateRoutes, url_prefix='/api/states')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)