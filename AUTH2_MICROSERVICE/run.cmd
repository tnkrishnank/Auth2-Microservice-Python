docker compose down --rmi all --volumes
docker compose up -d --build

@REM python -m venv .
@REM .\Scripts\activate
@REM pip install Flask
@REM pip install Flask-SQLAlchemy
@REM pip install flask-restx
@REM pip install PyMySQL
@REM pip install cryptography
@REM python run.py