FROM python:3.9

EXPOSE 5000

WORKDIR /env

COPY requirements.txt .

RUN pip install pymysql

RUN pip install -r ./requirements.txt

COPY . /env

ENTRYPOINT ["python"]

CMD ["main.py"]

