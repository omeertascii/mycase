FROM python:3.10-bullseye

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN git config --global url.ssh://git@github.com/.insteadOf https://github.com/
RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    gcc \
    gettext \
    libpq-dev \
    cron \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock /app
COPY pyproject.toml /app

RUN --mount=type=ssh poetry install

COPY ./src ./

# COPY ./entrypoint.sh ./

# RUN sed -i 's/\r$//g' /app/entrypoint.sh
# RUN chmod +x /app/entrypoint.sh

CMD python manage.py compilemessages --use-fuzzy && python manage.py collectstatic --no-input && python manage.py crontab add && python -m uvicorn app.asgi:application --host 0.0.0.0

EXPOSE 8000