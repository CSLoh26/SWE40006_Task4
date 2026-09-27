# --- Task 4.3 (Distinction) Dockerfile ---
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Environment variables have sensible defaults but are meant to be
# overridden at `docker run` time with -e flags
ENV APP_ENV=production
ENV PORT=5000
ENV APP_TITLE="Docker Distinction Demo"

EXPOSE 5000

CMD ["python", "app.py"]
