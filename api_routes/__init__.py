from flask import Flask
from api_routes import views

app = Flask(__name__)

app.config['ENV'] = 'production'
app.config['DEBUG'] = False
app.config['TESTING'] = False

# Register view
app.add_url_rule('/', view_func=views.HelloWorldView.as_view('hello_world'))