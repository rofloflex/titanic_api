# Базовый образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Сначала копируем только requirements.txt и устанавливаем зависимости
COPY ./titanic-api/requirements.txt /app
RUN pip3 install -r requirements.txt

# Копируем файлы проекта
COPY ./titanic-api /app

# Команда по умолчанию при запуске контейнера
CMD ["python3", "app_api.py"]