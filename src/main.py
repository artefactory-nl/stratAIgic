"""Server to host backend of app."""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world() -> str:
    """Hello World."""
    return "Hello, World!"


if __name__ == "__main__":
    app.run()