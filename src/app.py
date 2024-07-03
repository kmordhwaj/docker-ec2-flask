from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Docker Image for Flask on Ec2'

