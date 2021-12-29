from flask import Flask


def create_app():
    app = Flask(__name__, template_folder="../website/templates")
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    from .views import views
    # from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    # app.register_blueprint(auth, url_prefix='/')

    return app


app = create_app()
