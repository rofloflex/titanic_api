# Используем официальный облегчённый образ Python 3.10 в качестве базового
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Обновляем список пакетов и устанавливаем необходимые системные зависимости:
# build-essential - инструменты для сборки (gcc, make и т.д.)
# curl - для выполнения HTTP-запросов (нужно для HEALTHCHECK)
# software-properties-common - утилиты для управления репозиториями
# libgl1-mesa-glx - библиотека для OpenGL (может понадобиться для графических пакетов)
# После установки очищаем кэш apt для уменьшения размера образа
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Копируем только файл requirements.txt, чтобы максимально использовать кэш Docker при установке зависимостей
COPY ./streamlit-service/requirements.txt /app

# Устанавливаем Python-зависимости из requirements.txt
RUN pip3 install -r requirements.txt

# Копируем весь остальной код приложения в рабочую директорию контейнера
COPY /streamlit-service /app

# Открываем порт 8501, на котором Streamlit будет слушать запросы
EXPOSE 8501

# Настраиваем проверку состояния контейнера через HTTP-запрос к эндпоинту здоровья Streamlit
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Указываем команду, которая будет запускаться при старте контейнера:
# Запускаем Streamlit, указывая скрипт, порт и адрес для прослушивания всех интерфейсов
ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]