FROM python:3.12-slim

# RUN apt-get update && apt-get install -y

WORKDIR /app
COPY telegram/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY telegram/ ./

CMD ["python", "bot.py"]

# COPY requirements.txt /app/requirements.txt
# WORKDIR /app
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . /app/
# COPY bot.py bot.py

# CMD ["python", "bot.py"]
