
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Blue-Green Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 100px;
                background-color: #e8f5e9;
            }
            h1 {
                color: #2e7d32;
            }
            .version {
                display: inline-block;
                padding: 12px 24px;
                background-color: #2e7d32;
                color: white;
                border-radius: 8px;
            }
        </style>
    </head>
    <body>
        <h1>Flask Application Updated!</h1>
        <p>Welcome to Version 2 of our application.</p>
        <div class="version">GREEN VERSION - READY FOR TESTING</div>
        <p>Deployed on Amazon EKS using Argo Rollouts.</p>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
