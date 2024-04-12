from dotenv import load_dotenv
from flask import Flask, make_response
import os
from pymongo import MongoClient
import sys

# Load the environment variables
load_dotenv()

mongo_client = MongoClient(os.environ['MONGODB_URI'])

app = Flask(__name__)

@app.route('/')
def index():
    mongo_client.admin.command('ping')
    response = make_response(f"Hello World, successfully pinged mongodb", 200)
    response.mimetype = "text/plain"
    return response

if __name__ == '__main__':
    app.run(debug=True)
