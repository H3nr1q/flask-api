from flask import Flask
from flask_migrate import Migrate
from app.config import Config
from app import create_app, db
from app.routes import item_routes

migrate = Migrate()

def init_db():
    db.create_all()

app = create_app()

if __name__ == '__main__':
    app.register_blueprint(item_routes)  # Adicione esta linha
    app.run(debug=True)
