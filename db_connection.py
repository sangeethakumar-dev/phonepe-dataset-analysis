from sqlalchemy import create_engine

engine=create_engine("postgresql+psycopg2://postgres:sachumas123@localhost:5432/phonepe_db")

print("Connected to PostgreSQL Successfully")

 