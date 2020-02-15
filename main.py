import flask
from routes.home import home_page
from routes.repo import repo_page

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.register_blueprint(home_page)
app.register_blueprint(repo_page)

app.run(host='0.0.0.0', debug=True, port=5000)
