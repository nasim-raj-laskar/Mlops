from airflow import DAG                                                            
from airflow.providers.http.operators.http import HttpOperator  
from airflow.decorators import task             
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime, timedelta
import json

with DAG(
    dag_id="nasa_apod_postgres",
    start_date=datetime(2025, 9, 6),
    schedule="@daily",
    catchup=False,
    description="ETL pipeline to extract data from NASA APOD API and load into Postgres database",
) as dag:
    
    #step 1: Create table
    @task
    def create_table():
        #initialize Postgres hook
        postgres_hook = PostgresHook(postgres_conn_id='my_postgres_connection')

        ## SQL command to create table
        create_table_query="""
            CREATE TABLE IF NOT EXISTS apod_data (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255),
                explanation TEXT,
                url TEXT,
                date DATE,
                media_type VARCHAR(50)
            );
        """
        #execute SQL command
        postgres_hook.run(create_table_query)

    #step 2: Extract data from nasa API data (APOD)
    extract_apod = HttpOperator(
        task_id='extract_apod',
        http_conn_id='nasa_api',         #connection id define in Airflow For nasa Api
        endpoint='planetary/apod',       # Nasa api endpoit for apod
        method='GET',
        data={"api_key":"{{conn.nasa_api.extra_dejson.api_key}}"},      #using api key from connection
        response_filter=lambda response:response.json() ,    #convert response to json
        do_xcom_push=True
    )

    #step 3: Transform and load data (Pick the fields you want to load)

    @task
    def transform_apod_data(response):
        apod_data={
            'title':response.get('title',''),
            'explanation':response.get('explanation',''),
            'url':response.get('url',''),
            'date':response.get('date',''),
            'media_type':response.get('media_type',''),
        }
        return apod_data

    #step 4: Load data into Postgres SQL database

    @task
    def load_data_to_postgres(apod_data):
        #initialize Postgres hook
        postgres_hook = PostgresHook(postgres_conn_id='my_postgres_connection')
        
        #Define the SQL query to insert data

        insert_query="""
            INSERT INTO apod_data (title, explanation, url, date, media_type)
            VALUES (%s, %s, %s, %s, %s);
        """
        #execute the sql query
        postgres_hook.run(insert_query, parameters=(
            apod_data['title'],
            apod_data['explanation'],
            apod_data['url'],
            apod_data['date'],
            apod_data['media_type']
        ))


    #step 5: Verify the data DBViewer

    #step 6: define the task dependencies
    #extract     E
    #transform   T
    #load        L
    #ETL

    create_table()>>extract_apod
    api_response=extract_apod.output
    transform_apod=transform_apod_data(api_response)
    load_data_to_postgres(transform_apod)
