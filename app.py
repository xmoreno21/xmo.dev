from flask import Flask, request, render_template, send_file, redirect
import Config


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return "Lockr is running!"