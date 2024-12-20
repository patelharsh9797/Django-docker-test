FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc6-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*


# Install Python dependencies
COPY requirements.txt .
RUN python -m venv /venv \
    && /venv/bin/pip install --upgrade pip \
    && /venv/bin/pip install --no-cache-dir --default-timeout=20000 --retries 50 -r requirements.txt


ENV PATH="/venv/bin:$PATH"

COPY . .

WORKDIR /app
COPY ./src .

EXPOSE 8000

COPY ./entrypoint.sh .
CMD [ "sh", "./entrypoint.sh" ]

