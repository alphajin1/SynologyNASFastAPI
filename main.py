import sqlalchemy as db
from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()
USER_NAME = os.environ.get("USER_NAME")
PASSWORD = os.environ.get("PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
HOST_NAME = os.environ.get("HOST_NAME")
engine = db.create_engine(f"mysql+pymysql://{USER_NAME}:{PASSWORD}@{HOST_NAME}/{DB_NAME}?charset=utf8")
connection = engine.connect()
metadata = db.MetaData()
test_table = db.Table('test', metadata, autoload=True, autoload_with=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/message/{msg_id}")
def read_message(msg_id: int):
    query = test_table.select().where(test_table.c.id == msg_id)
    with engine.connect() as conn:
        result_proxy = conn.execute(query)
        result_set = result_proxy.fetchone()
        return {"msg_id": result_set}

    return {}
