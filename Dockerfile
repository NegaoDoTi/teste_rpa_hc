FROM python:3.10-slim
WORKDIR /robot
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod +x ./wait-for-it.sh
CMD ["python", "run.py"]