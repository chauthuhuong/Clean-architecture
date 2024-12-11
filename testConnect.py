from sqlalchemy import create_engine
connection_string = (
    "mssql+pyodbc://sa:123@DESKTOP-7ULF75N\ROOT/TestORM?"
    "driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
)

try:
    engine = create_engine(connection_string)
    with engine.connect() as connection:
        print("Connected!")
except Exception as e:
    print("Failed:", e)
