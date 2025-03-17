FROM python:3.12 as python-base

workdir /PythonProject

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot-main.py"]