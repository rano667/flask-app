FROM python:3.13.4-slim-bookworm
WORKDIR /docker

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY ./ ./

CMD ["python", "-m", "flask", "--app", "loan", "run", "--host", "0.0.0.0", "--port", "8080"]