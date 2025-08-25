from flask import Flask
from routes.route import route_bp
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

# Registro do blueprint
app.register_blueprint(route_bp, url_prefix='/api')

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(host='localhost', port=port)
