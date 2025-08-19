from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return "<h1>Welcome to My DevOps CI/CD Project 🚀</h1>"

@app.get("/status")
def status():
    return jsonify(ok=True, message="CI pipeline healthy")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
