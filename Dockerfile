FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN useradd --create-home --shell /bin/bash app_user

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

USER app_user
COPY . /code/
