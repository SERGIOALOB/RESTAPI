FROM python:3.9


COPY . /env

WORKDIR /env

RUN pip install -r ./requirements.txt
ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["main.py"]