# -*- coding: utf-8 -*-

# -----------------------------------------------------------
# NewsAPI - v1.0
# Módulo para buscar notícias do NewsAPI.org
#
# 2021 Edgard H. Santos Lopes, Bahia, Brasil
# email edgardhwp@outlook.com
# -----------------------------------------------------------
from flask import Flask
app = Flask("News");

from news_routes import newsRoutes
app.register_blueprint(newsRoutes, url_prefix='/api/news')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)