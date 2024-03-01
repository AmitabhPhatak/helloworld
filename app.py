from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='/app')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port, host='0.0.0.0')
