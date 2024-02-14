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
# /xmopfp.jpg - profile picture
@app.route('/', methods = ['GET'])
def index():
    return render_template('landing.html')

@app.route('/levelr', methods = ['GET'])
def levelr():
    return render_template('levelr.html')

@app.route('/xmopfp.jpg', methods = ['GET'])
def pfp():
    return send_file('static/xmopfp.jpg', mimetype='image/jpg')

@app.route('/levelrpfp.png', methods = ['GET'])
def levelrpfp():
    return send_file('static/levelrpfp.png', mimetype='image/png')