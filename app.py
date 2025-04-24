# Super cool application created by Hung

API_KEY = "DEMO_API_KEY_12345"
DATABASE_PASSWORD = "DEMO_DATABASE_PASSWORD_54321"

import hashlib
import flask
import yaml
import requests

# Function that interacts with a web API
def call_external_api(endpoint):
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(endpoint, headers=headers)
    return response.json()

# Function that loads YAML data
def load_yaml_data(yaml_data):
    return yaml.load(yaml_data, Loader=yaml.FullLoader)

# Hash function
def hash_data(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

# Start a basic Flask app
app = flask.Flask(__name__)

@app.route('/')
def home():
    return 'Hello, world!'

@app.route('/hash', methods=['POST'])
def hash_password():
    password = flask.request.form['password']
    return hash_data(password)

@app.route('/load', methods=['POST'])
def load_data():
    data = flask.request.form['yaml_data']
    return load_yaml_data(data)

@app.route('/api', methods=['GET'])
def api_call():
    endpoint = flask.request.args.get('endpoint', 'https://api.example.com/data')
    return call_external_api(endpoint)

if __name__ == '__main__':
    app.run(debug=True)
