<<<<<<< HEAD
from flask import Flask, send_from_directory, render_template
from flask_cors import CORS
from config import Config
from routes.book_routes import book_bp
import os
=======
from flask import Flask
from flask_cors import CORS
from config import Config
from routes.book_routes import book_bp
>>>>>>> 0eade81c7ef95c78542c132cb905eb3790e63584

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['JSON_AS_ASCII'] = False
    
    CORS(app)
    
    app.register_blueprint(book_bp, url_prefix='/api/books')
    
<<<<<<< HEAD
    @app.route('/')
    def serve_index():
        return render_template('index.html')

    @app.route('/history')
    def history_page():
        return render_template('history.html')

=======
>>>>>>> 0eade81c7ef95c78542c132cb905eb3790e63584
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)