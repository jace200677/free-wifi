from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/')
def portal():
    # Fetch remote HTML from GitHub Pages
    r = requests.get('https://jace200677.github.io/free-wifi/templates/index.html')
    return Response(r.text, mimetype='text/html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
