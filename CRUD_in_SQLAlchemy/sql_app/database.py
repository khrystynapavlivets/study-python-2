import os

from sqlalchemy import create_engine  # це функція, яка створює об’єкт “двигуна” (engine) для взаємодії з базою даних.
from sqlalchemy.orm import declarative_base, \
    sessionmaker  # створює базовий клас для ORM-моделе, створює базовий клас для ORM-моделей.
from dotenv import load_dotenv

load_dotenv()

# Налаштування підключення до бази даних
SQLALCHEMY_DATABASE_URL = os.environ.get("POSTGRESQL")  # Для PostgreSQL

# Створення об'єкта двигуна (engine) для підключення до БД
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Створення сесії для взаємодії з БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовий клас для створення моделей
Base = declarative_base()


