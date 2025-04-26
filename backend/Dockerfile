FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
# Ensure the main.py file exists and contains an ASGI app named 'app'
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]