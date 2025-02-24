from flask import Flask
from config import HOST, PORT, DEBUG
from routes.Router import Router
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def index():
    return '<h1>REST API successfully running</h1>'


Router.run(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
