from flask import Flask
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/")
def home():
    current_time = datetime.now(timezone.utc).strftime("%H:%M:%S UTC")

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>CloudDeploy</title>

        <style>
            * {{
                box-sizing: border-box;
            }}

            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #2563eb, #7c3aed);
                color: #1e293b;
                min-height: 100vh;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }}

            .card {{
                background: white;
                max-width: 600px;
                width: 100%;
                padding: 40px 30px;
                border-radius: 20px;
                text-align: center;
                box-shadow: 0 15px 40px #00000030;
            }}

            h1 {{
                color: #2563eb;
                font-size: 2.5rem;
                margin-bottom: 12px;
            }}

            .description {{
                color: #64748b;
                line-height: 1.7;
                margin-bottom: 28px;
            }}

            .time-box {{
                background: #eff6ff;
                border: 1px solid #bfdbfe;
                border-radius: 12px;
                padding: 18px;
                margin: 20px 0;
            }}

            .time-box h3 {{
                color: #1d4ed8;
                margin-top: 0;
            }}

            .time {{
                font-size: 1.4rem;
                font-weight: bold;
                color: #7c3aed;
            }}

            .tags {{
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 10px;
                margin-top: 25px;
            }}

            .tag {{
                background: #ede9fe;
                color: #5b21b6;
                padding: 8px 12px;
                border-radius: 20px;
                font-size: 0.85rem;
                font-weight: bold;
            }}

            footer {{
                color: #94a3b8;
                font-size: 0.85rem;
                margin-top: 28px;
            }}
        </style>
    </head>

    <body>
        <main class="card">
            <h1>CloudDeploy</h1>

            <p class="description">
                A simple Flask application built with Docker
                and deployed using AWS and Kubernetes.
            </p>

            <div class="time-box">
                <h3>Current Server Time</h3>
                <div class="time" id="clock">{current_time}</div>
            </div>

            <div class="tags">
                <span class="tag">Python</span>
                <span class="tag">Flask</span>
                <span class="tag">Docker</span>
                <span class="tag">AWS</span>
                <span class="tag">Kubernetes</span>
            </div>

            <footer>
                Powered by Flask · Cloud Deployment Lab
            </footer>
        </main>

        <script>
            function updateClock() {{
                document.getElementById("clock").textContent =
                    new Date().toISOString().slice(11, 19) + " UTC";
            }}

            updateClock();
            setInterval(updateClock, 1000);
        </script>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
