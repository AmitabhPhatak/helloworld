from flask import Flask
import os
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('/projects/index.html')


if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')