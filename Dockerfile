FROM python:3.9


WORKDIR /env

COPY . /env

RUN pip install -r ./requirements.txt

ENTRYPOINT FLASK_APP=/env/main.py flask run --host=0.0.0.0
