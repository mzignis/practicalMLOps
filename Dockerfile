FROM python:3.11

COPY . /app
WORKDIR /app

RUN make install

CMD ["python", "main.py"]
