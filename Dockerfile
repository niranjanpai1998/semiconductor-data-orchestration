FROM apache/airflow:2.7.0

USER root 

# Install PostgreSQL development packages
RUN apt-get update && \
    apt-get install -y libpq-dev && \
    rm -rf /var/lib/apt/lists/* 


# Copy requirements.txt into the image
COPY requirements.txt .

USER airflow

# Install dependencies as the airflow user
RUN pip install --no-cache-dir -r requirements.txt
