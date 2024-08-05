# Используем облегченный базовый образ
FROM python:3.12-slim

# Определяем рабочую директорию
WORKDIR /app

# Копируем файлы
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Открываем порт
EXPOSE 8501

# Команда для запуска приложения
CMD ["streamlit", "run", "--server.port", "8501", "main.py"]
