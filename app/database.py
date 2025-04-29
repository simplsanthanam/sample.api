from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from sqlalchemy.dialects import registry
import psycopg
from psycopg.rows import dict_row
from.import models,schemas,utils
import time
from .config import settings


password = quote_plus("Soundarya89$")
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

#SQLALCHEMY_DATABASE_URL='postgresql://postgres:Soundarya89$@localhost/fastapi'

from sqlalchemy.dialects import registry
registry.register("postgresql.psycopg", "psycopg.sqlalchemy", "dialect")

def get_db():
    db=session_local()
    try:
        yield db
    finally:
        db.close()
        
engine=create_engine(SQLALCHEMY_DATABASE_URL)
session_local=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()

# while True :
#     try:
#     #conn=psycopg.connect (host='localhost',dbname='fastapi',user='postgres',password='Soundarya89$',
#       #                    cursor_factory=dict_row)
#         conn = psycopg.connect(
#         host='localhost',
#         dbname='fastapi',
#         user='postgres',
#         password='Soundarya89$')
#         conn.row_factory = dict_row  
#         cursor= conn.cursor()
#         print("database connection sucessful")
#         break
#     except Exception as error:
#         print("not connected")
#         print("error was", error)
#         time.sleep(2)
