FROM python:3.11-slim

WORKDIR /app

COPY . /app/

RUN pip isntall --upgrade pip && \
    pip install -r requirements.txt

CMD [ "pytest" ]