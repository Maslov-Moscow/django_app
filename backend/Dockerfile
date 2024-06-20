FROM python:3.12-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY . /app/

EXPOSE 8000/tcp

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]