from python:3.11-slim
WORKDIR /etl
copy requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
copy . .
CMD ["python", "code.py"]