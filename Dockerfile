FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ .

CMD ["python", "main.py"]

# Start from a lightweight Python base image (python:3.10-slim).
# Set working directory to /app.
# Copy your requirements.txt and install dependencies.
# Copy your app/ folder (containing main.py and model.pkl).
# Set the default command: python main.py.
