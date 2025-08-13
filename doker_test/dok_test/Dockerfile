# Базовый Python-образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /code

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Открываем порт
EXPOSE 8000


