# run.py

from flask import Flask
from flask_migrate import Migrate
from app.config import Config
from app import create_app, db
from app.routes import item_routes

migrate = Migrate()

def init_db():
    db.create_all()

app = create_app(Config)

@app.before_first_request
def create_tables():
    init_db()

@app.after_request
def save_session(response):
    db.session.remove()
    return response

if __name__ == '__main__':
    app.run(debug=True)
