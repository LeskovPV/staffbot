from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    return '<p>Hello Flask!</p>'


if __name__ == '__main__':
    app.run(debug=False)
