import re
import pandas as pd
from sqlalchemy import create_engine, text

# 1. Loading Excel file (absolute path)
excel_path = r"C:\Users\Go to your excel file\Copy as path\paste here\sentiment_analysis_all\sentiment_analysis.xlsx"
df = pd.read_excel(excel_path)

# 2. PostgreSQL Connection
db_user = 'postgres'
db_password = 'Your Password'   # replace with your actual password
db_host = 'localhost'
db_port = '5432'
db_name = 'postgres'

# Creating engine (Do not change this line)
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# 3. Schema creation
with engine.connect() as conn:
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS analysis;"))
    conn.commit()

# 4. Cleaning Column names
df.columns = [
    re.sub(r'[^a-z0-9_]', '', str(col).strip().lower().replace(" ", "_").replace(".", "_"))
    for col in df.columns
]

# 5. Cleaning Rows
def clean_row_data(value):
    if not isinstance(value, str):
        return value
    
    cleaned = value.strip()
    cleaned = cleaned.lower()
    cleaned = re.sub(
        r'[\$\u20A0-\u20CF\u00A2\u00A3\u00A4\u00A5\U0001F4B5\U0001F4B4\U0001F4B0\+\@\#\%\^\*]',
        '',
        cleaned
    )
    cleaned = re.sub(r'\s+', '_', cleaned)
    cleaned = cleaned.strip('_')
    
    return cleaned

# 6. Apply cleaning function column by column
for col in df.columns:
    df[col] = df[col].map(clean_row_data)

# 7. Loading data into the database (With accurate data types)
from sqlalchemy import types 

try:
    df.to_sql(
        name='sentiment_analysis',
        con=engine,
        schema='analysis',
        if_exists='replace',
        index=False,
        method='multi',
   dtype={
    'year': types.SmallInteger(),
    'month': types.SmallInteger(),
    'day': types.SmallInteger(),
    'time_of_tweet': types.Text(),
    'text': types.Text(),
    'sentiment': types.Text(),
    'platform': types.VARCHAR(30)
}
    )
    print("Your data has been moved from Excel to PostgreSQL with custom types")
except Exception as e:
    print(f"An error occurred: {e}")

