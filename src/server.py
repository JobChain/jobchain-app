from flask import Flask, render_template
import random
app = Flask(__name__, template_folder='./static')

@app.route("/")
def index():
    return "Jobchain"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)