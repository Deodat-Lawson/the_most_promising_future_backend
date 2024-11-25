FROM python:3.11-bookworm

# Install system dependencies
RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Collect static files
COPY . .

CMD gunicorn the_most_promising_future_backend.wsgi:application --bind 0.0.0.0:8000
EXPOSE 8000