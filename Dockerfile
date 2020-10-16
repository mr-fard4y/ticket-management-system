FROM python:3.8-slim

RUN pip3 install pipenv

WORKDIR /usr/src/app
COPY Pipfile* ./
RUN pipenv install

COPY . .

EXPOSE 8000

CMD [ "pipenv", "run", "gunicorn", "-b 0.0.0.0:8000", "manage:app" ]