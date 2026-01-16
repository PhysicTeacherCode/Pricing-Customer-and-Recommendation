import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# carregar variáveis de ambiente
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine_db = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

df = pd.read_excel("../data/Online Retail.xlsx")

df.columns = (
    df.columns
      .str.strip() # retire espaços
      .str.replace('([a-z])([A-Z])', r'\1_\2', regex=True) # adiciona '_' entre letras
      .str.lower() # tudo em minúscula
)

df.to_sql(
    name="online_retail",
    con=engine_db,
    if_exists="replace",
    index=False
)

display(df.head(20))