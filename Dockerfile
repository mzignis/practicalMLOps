FROM python:3.11

COPY . /app
WORKDIR /app

RUN python3 -m venv venv
ENV PATH="/app/venv/bin:$PATH"
RUN make install

CMD ["python", "main.py"]
