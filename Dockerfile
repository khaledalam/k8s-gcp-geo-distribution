FROM python:3.9

LABEL maintainer="khaledalam.net@gmail.com"

WORKDIR /code

COPY ./app/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

# RUN sed 's/APP_COUNTRY=.*/APP_COUNTRY="$APP_COUNTRY"/g' .env.sample > tmpenv ; mv tmpenv .env.sample

# Rename file .env.sample to .env
RUN mv /code/app/.env.sample /code/app/.env

CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "80"]