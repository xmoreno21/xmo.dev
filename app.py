from flask import Flask, request, render_template, send_file, redirect
import Config


app = Flask(__name__)

# /: biolink, general xmo information
# /levelr - levelr landing page with link to docs and status pages
# /levelr/docs - levelr documentation
# /levelr/status - levelr status page
# /lockr - lockr landing page with link to docs and status pages
# /lockr/docs - lockr documentation
# /lockr/status - lockr status page
# /soundsworld - sw invite redirect

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/pfp.jpg', methods = ['GET'])
def pfp():
    return send_file('static/pfp.jpg', mimetype='image/jpg')