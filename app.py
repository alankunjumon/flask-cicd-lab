from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Flask Docker Lab</h1>
    <p>Your first containerized Python application is running.</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
