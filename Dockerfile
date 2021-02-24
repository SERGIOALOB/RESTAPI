FROM python:3.9

EXPOSE 5000

RUN mkdir /app

WORKDIR /app

COPY app/requirements.txt /app/requirements.txt

RUN pip install pymysql

RUN pip install -r ./requirements.txt

COPY app /app

ENTRYPOINT ["python"]

CMD ["main.py"]
