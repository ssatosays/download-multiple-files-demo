import os

from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/get', methods=['GET'])
def get():
    file_name = request.args.get('file_name')
    return send_from_directory(
        os.path.join(app.root_path, 'static/pdf'),
        file_name,
        mimetype='application/pdf')


if __name__ == '__main__':
    app.run()
