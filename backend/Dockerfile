# Use the official lightweight Python image.
FROM python:3.9-slim

# Copy local code to the container image.

WORKDIR /app

COPY requirements.txt requirements.txt
# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run the web service on container startup.
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]