FROM --platform=linux/amd64 python:3.12.7-slim

# Create a non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /opt/ai-agent/

RUN mkdir src

COPY src ./src
COPY .env ./
COPY config.yaml ./config.yaml
COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Set permission for the directories
RUN chown -R appuser:appuser /opt/ai-agent/

# Switch to non-root user
USER appuser

CMD ["python3", "src/main.py"]
