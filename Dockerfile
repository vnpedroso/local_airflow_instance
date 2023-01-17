FROM apache/airflow:2.4.1

USER root

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \ 
		nano \
	&& apt-get autoremove -yqq --purge \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

USER airflow

RUN python -m pip install --upgrade pip 

COPY requirements.txt /

RUN pip install --no-cache-dir -r /requirements.txt

COPY ./dags /opt/airflow/dags/