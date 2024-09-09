import pandas as pd
import psycopg2
from sqlalchemy import create_engine, text

#df = pd.read_csv('acidentes2017.csv', sep=';', verbose=True, encoding='latin-1')
#df = pd.read_csv('acidentes2018.csv', sep=';', verbose=True, encoding='latin-1')
#df = pd.read_csv('acidentes2019.csv', sep=';', verbose=True, encoding='latin-1')
#df = pd.read_csv('acidentes2020.csv', sep=';', verbose=True, encoding='latin-1')
#df = pd.read_csv('acidentes2021.csv', sep=';', verbose=True, encoding='latin-1')
#df = pd.read_csv('acidentes2022.csv', sep=';', verbose=True, encoding='latin-1')
#df = pd.read_csv('acidentes2023.csv', sep=';', verbose=True, encoding='latin-1')

# Define the database connection parameters
db_params = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres'
}

conn = psycopg2.connect(
    host=db_params['host'],
    database=db_params['database'],
    user=db_params['user'],
    password=db_params['password']
)

# Connect to the 'soccer' database
db_params['database'] = 'teste'
engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}/{db_params["database"]}')

# Define the file paths for your CSV files
csv_files = {
    'teste1': './acidentes2023.csv',
    'teste2': './acidentes2022.csv',
    'teste3': './acidentes2021.csv',
    'teste4': './acidentes2020.csv',
    'teste5': './acidentes2019.csv',
    'teste6': './acidentes2018.csv',
    'teste7': './acidentes2017.csv',
}

# Loop through the CSV files and import them into PostgreSQL
for table_name, file_path in csv_files.items():
    #print(table_name, file_path)
    df = pd.read_csv(file_path, sep=';', encoding='latin-1')
    df.to_sql('teste1', engine,if_exists='append', index=False)