FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install poetry
RUN pip install poetry==1.8.3

# Copy only requirements first to leverage Docker cache
COPY poetry.lock pyproject.toml ./

# Install dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-root

# Copy the rest of the application
COPY . .

# Set Python path
ENV PYTHONPATH=/app

CMD ["python", "-m", "src.main"]
