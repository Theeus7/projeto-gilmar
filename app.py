from flask import Flask
from flask_cors import CORS
from config import Config
from routes.book_routes import book_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['JSON_AS_ASCII'] = False
    
    CORS(app)
    
    app.register_blueprint(book_bp, url_prefix='/api/books')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)