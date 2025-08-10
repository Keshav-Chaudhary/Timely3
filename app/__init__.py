import os
import json
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'data'))
JSON_FILE = os.path.join(DATA_DIR, 'timetable.json')

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Initialize empty JSON if not exists
if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump({"timetable": {}}, f, indent=4)

def load_timetable():
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_timetable(data):
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'devkey')

    app.load_timetable = load_timetable
    app.save_timetable = save_timetable
    app.JSON_FILE = JSON_FILE

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
