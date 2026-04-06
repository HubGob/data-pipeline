FROM python:3.11-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --without dev --no-interaction --no-ansi

COPY src/ ./src/
COPY data/ ./data/

ENV PYTHONPATH=/app

CMD ["python", "src/pipeline/load.py"]
