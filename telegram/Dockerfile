FROM python:3.11-slim

# RUN apt-get update && apt-get install -y

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
COPY bot.py bot.py

CMD ["python", "bot.py"]
