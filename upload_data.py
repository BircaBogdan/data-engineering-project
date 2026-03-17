import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# încarcă variabilele din .env
load_dotenv()

# dataset demo
data = {
    "product": ["Laptop", "Mouse", "Keyboard"],
    "price": [1200, 25, 70],
    "quantity": [2, 10, 5]
}

df = pd.DataFrame(data)

# citire credențiale din variabile de mediu
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

# conexiune securizată
engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
)

# upload date
df.to_sql("sales", engine, if_exists="replace", index=False)

print("Data uploaded to AWS RDS!")