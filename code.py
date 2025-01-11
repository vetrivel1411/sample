from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the Flask Server!</h1><p>This is a simple server example.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
