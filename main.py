from flask import Flask
from controllers.one_controller import one_bp
from controllers.two_controller import two_bp
from controllers.health_check import health_check_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(one_bp, url_prefix='/model_1')
app.register_blueprint(two_bp, url_prefix='/model_2')
app.register_blueprint(health_check_bp, url_prefix='/health')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
