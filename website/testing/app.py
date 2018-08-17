from flask import Flask

def create_app():
    
    app = Flask(__name__)
    
    app.config.from_mapping(SECRET_KEY = 'dev')
    
    @app.route('/')
    def hi():
        return 'hi'
    
    from main_form import bp
    app.register_blueprint(bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()