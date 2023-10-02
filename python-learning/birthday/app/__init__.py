from flask import Flask , render_template
from app.main.events import event_bp
from app.main.birthdays import birthdays_bp # Import Blueprints from 'routes' package
from app.extensions import db
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)  # Load configuration from 'config.py'
    # Register Blueprints with the app
    app.register_blueprint(birthdays_bp)
    app.register_blueprint(event_bp)

    db.init_app(app)  # Initialize SQLAlchemy with the Flask app

    @app.route('/')
    def index():
        from app.models.post import Birthday
        birthdays = Birthday.query.all()
        return render_template('create_birthday.html', birthdays=birthdays)

    return app


if __name__ == '__main__':
    app.run(debug=True)