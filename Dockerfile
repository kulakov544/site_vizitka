# Используем базовый образ Python
FROM python:3.12

# Устанавливаем Streamlit
RUN pip install streamlit

# Устанавливаем дополнительные зависимости (если нужно)
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# Копируем код вашего приложения в контейнер
COPY . /app
WORKDIR /app

# Определяем порт, который использует Streamlit (по умолчанию 8501)
EXPOSE 8501

# Команда для запуска Streamlit приложения
CMD ["streamlit", "run", "--server.port", "8501", "resume.py"]

