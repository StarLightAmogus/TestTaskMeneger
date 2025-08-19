FROM python:3.11-slim

WORKDIR /app

# Устанавливаем зависимости Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем Gauge + плагин Python
RUN apt-get update && apt-get install -y curl unzip git \
    && curl -SsL https://downloads.gauge.org/stable | sh \
    && gauge install python

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
