FROM python:3.9

# EXPOSE 8000

# 1. Install essential packages
RUN apt-get update \
    && apt-get install -y \
        build-essential \
        cmake \
        wget \
        unzip \
        unixodbc-dev \
        gcc \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# 2. Copy the whole project to /sanka
WORKDIR /classmanagement
COPY . /classmanagement

# 3. Install packages in requirements.txt
RUN python -m pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "classmanagement.wsgi"]

