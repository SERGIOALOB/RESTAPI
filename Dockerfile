FROM python:3.9

RUN pip3 install pipenv

ENV DockerApi /usr/src/flaskbookapi

WORKDIR DockerApi

COPY Pipfile .
COPY Pipfile.lock .
COPY . .

RUN pipenv install --system --deploy --ignore-pipfile
RUN pip3 install flask
RUN pip3 install flask-restful
EXPOSE 5000

CMD ["pipenv", "run", "python", "api.py"]