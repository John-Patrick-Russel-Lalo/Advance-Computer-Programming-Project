# app.py
from app_instance import app
from routes import *  # Import routes after the app instance is created

if __name__ == '__main__':
    app.run(debug=True)