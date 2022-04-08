FROM python:3.7-slim

WORKDIR /app/book

RUN pip install --upgrade --no-cache pip
RUN pip install psycopg2-binary

COPY setup.cfg setup.py ./

RUN pip install --no-cache-dir -e .[dev]

#COPY requirements.txt .
#RUN pip install -r requirements.txt

COPY . .

WORKDIR /app

# RUN pip install hupper waitress

# CMD ["python", "run_api.py"]

