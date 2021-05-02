FROM python:3.9.4-slim-buster
WORKDIR /code
COPY requirements.txt /code/
ENV PYTHONPYCACHEPREFIX="$HOME/.cache/cpython/"
RUN pip install -r requirements.txt
COPY . /code/
CMD [ "python", "./app/app.py" ]