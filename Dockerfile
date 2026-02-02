FROM cgr.dev/chainguard/python:latest-dev AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM cgr.dev/chainguard/python:latest

WORKDIR /app

COPY --from=builder /home/nonroot/.local /home/nonroot/.local

COPY app.py .
COPY resume_config.toml .
COPY templates/ templates/
COPY static/ static/

EXPOSE 8000

ENTRYPOINT ["python", "-m", "gunicorn", "-b", "0.0.0.0:8000", "app:app"]
