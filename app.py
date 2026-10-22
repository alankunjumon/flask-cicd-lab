
from flask import Flask, render_template_string, jsonify
from datetime import datetime, timezone
import os

app = Flask(__name__)

APP_NAME = "CloudDeploy"
APP_VERSION = os.getenv("APP_VERSION", "v2.0.0")
APP_ENV = os.getenv("APP_ENV", "STAGING").upper()


@app.route("/")
def home():
    current_time = datetime.now(timezone.utc).strftime("%H:%M:%S UTC")

    return render_template_string(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta name="theme-color" content="#0b1120">
            <title>{{ app_name }} | Cloud Operations</title>

            <style>
                :root {
                    --bg: #0b1120;
                    --panel: #111a2e;
                    --border: #253451;
                    --text: #e5edf9;
                    --muted: #8fa2c1;
                    --blue: #60a5fa;
                    --purple: #a78bfa;
                    --green: #34d399;
                }

                * {
                    box-sizing: border-box;
                }

                body {
                    margin: 0;
                    min-height: 100vh;
                    background:
                        radial-gradient(ellipse at 15% 0%,
                            #1e3a8a55, transparent 42%),
                        radial-gradient(ellipse at 90% 20%,
                            #6d28d933, transparent 38%),
                        var(--bg);
                    color: var(--text);
                    font-family: Inter, ui-sans-serif, system-ui,
                        -apple-system, BlinkMacSystemFont, "Segoe UI",
                        sans-serif;
                }

                .container {
                    max-width: 1180px;
                    margin: auto;
                    padding: 28px 24px 40px;
                }

                header {
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    gap: 18px;
                    padding-bottom: 26px;
                    border-bottom: 1px solid var(--border);
                }

                .brand {
                    display: flex;
                    align-items: center;
                    gap: 13px;
                }

                .logo {
                    width: 46px;
                    height: 46px;
                    display: grid;
                    place-items: center;
                    border-radius: 14px;
                    color: white;
                    font-weight: 900;
                    font-size: 23px;
                    background: linear-gradient(135deg, #3b82f6, #8b5cf6);
                    box-shadow: 0 7px 25px #3b82f633;
                }

                h1, h2, p {
                    margin-top: 0;
                }

                .brand h1 {
                    margin-bottom: 3px;
                    font-size: 20px;
                    letter-spacing: -0.5px;
                }

                .subtitle, .muted {
                    color: var(--muted);
                }

                .subtitle {
                    margin: 0;
                    font-size: 12px;
                }

                .environment {
                    display: inline-flex;
                    align-items: center;
                    gap: 8px;
                    border: 1px solid #92400e;
                    border-radius: 999px;
                    padding: 9px 13px;
                    background: #78350f33;
                    color: #fbbf24;
                    font-size: 11px;
                    font-weight: 800;
                    letter-spacing: 1px;
                }

                .dot {
                    width: 7px;
                    height: 7px;
                    display: inline-block;
                    border-radius: 50%;
                    background: var(--green);
                    box-shadow: 0 0 10px #34d39988;
                }

                .hero {
                    padding: 48px 0 30px;
                }

                .eyebrow {
                    color: var(--blue);
                    text-transform: uppercase;
                    font-size: 11px;
                    font-weight: 800;
                    letter-spacing: 2px;
                    margin-bottom: 14px;
                }

                .hero h2 {
                    font-size: clamp(30px, 5vw, 48px);
                    line-height: 1.12;
                    letter-spacing: -1.7px;
                    margin-bottom: 16px;
                }

                .gradient-text {
                    background: linear-gradient(90deg, #60a5fa, #c4b5fd);
                    background-clip: text;
                    -webkit-background-clip: text;
                    color: transparent;
                }

                .hero p {
                    max-width: 650px;
                    color: var(--muted);
                    font-size: 15px;
                    line-height: 1.8;
                    margin-bottom: 0;
                }

                .section-heading {
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    gap: 12px;
                    margin: 18px 0;
                }

                .section-heading h3 {
                    font-size: 15px;
                    margin: 0;
                }

                .section-heading span {
                    color: var(--muted);
                    font-size: 11px;
                }

                .grid {
                    display: grid;
                    grid-template-columns: repeat(3, minmax(0, 1fr));
                    gap: 16px;
                }

                .panel {
                    min-width: 0;
                    padding: 22px;
                    border: 1px solid var(--border);
                    border-radius: 17px;
                    background: linear-gradient(
                        145deg, #17233be8, #10182ae8
                    );
                    box-shadow: 0 12px 30px #00000012;
                }

                .card-top {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    gap: 10px;
                    margin-bottom: 22px;
                }

                .card-label {
                    color: var(--muted);
                    font-size: 12px;
                }

                .icon {
                    display: grid;
                    place-items: center;
                    width: 38px;
                    height: 38px;
                    border: 1px solid var(--border);
                    border-radius: 12px;
                    background: #ffffff08;
                    font-size: 17px;
                }

                .metric {
                    font-size: clamp(21px, 3vw, 28px);
                    font-weight: 750;
                    letter-spacing: -0.8px;
                    overflow-wrap: anywhere;
                }

                .metric-note {
                    color: var(--muted);
                    font-size: 11px;
                    margin-top: 9px;
                }

                .green {
                    color: var(--green);
                }

                .blue {
                    color: var(--blue);
                }

                .purple {
                    color: var(--purple);
                }

                .time-panel {
                    margin-top: 16px;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    gap: 20px;
                }

                .time-panel h3 {
                    font-size: 15px;
                    margin-bottom: 8px;
                }

                .time-panel p {
                    color: var(--muted);
                    font-size: 12px;
                    line-height: 1.6;
                    margin-bottom: 0;
                }

                .clock {
                    color: var(--blue);
                    font-size: clamp(23px, 4vw, 34px);
                    font-weight: 750;
                    font-variant-numeric: tabular-nums;
                    letter-spacing: 1px;
                    white-space: nowrap;
                }

                .deployment {
                    margin-top: 16px;
                }

                .deployment h3 {
                    font-size: 15px;
                    margin-bottom: 20px;
                }

                .details {
                    display: grid;
                    grid-template-columns: repeat(3, minmax(0, 1fr));
                    gap: 20px;
                }

                .detail-label {
                    color: var(--muted);
                    font-size: 11px;
                    margin-bottom: 8px;
                }

                .detail-value {
                    font-size: 13px;
                    font-weight: 650;
                    overflow-wrap: anywhere;
                }

                .stack {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 9px;
                }

                .tag {
                    padding: 8px 12px;
                    border: 1px solid #35476a;
                    border-radius: 9px;
                    color: #c7d7f2;
                    background: #192640;
                    font-size: 11px;
                    font-weight: 650;
                }

                footer {
                    margin-top: 28px;
                    padding-top: 20px;
                    border-top: 1px solid var(--border);
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: space-between;
                    gap: 12px;
                    color: var(--muted);
                    font-size: 11px;
                }

                @media (max-width: 760px) {
                    .grid {
                        grid-template-columns: 1fr;
                    }

                    .details {
                        grid-template-columns: 1fr;
                        gap: 18px;
                    }

                    .hero {
                        padding-top: 36px;
                    }

                    .time-panel {
                        align-items: flex-start;
                        flex-direction: column;
                    }
                }

                @media (max-width: 440px) {
                    .container {
                        padding: 20px 15px 30px;
                    }

                    header {
                        align-items: flex-start;
                    }

                    .environment {
                        font-size: 9px;
                        padding: 8px 9px;
                    }

                    .brand h1 {
                        font-size: 17px;
                    }

                    .logo {
                        width: 39px;
                        height: 39px;
                    }
                }
            </style>
        </head>

        <body>
            <div class="container">
                <header>
                    <div class="brand">
                        <div class="logo">C</div>
                        <div>
                            <h1>{{ app_name }}</h1>
                            <p class="subtitle">Cloud Operations Dashboard</p>
                        </div>
                    </div>

                    <div class="environment">
                        <span class="dot"></span>
                        {{ environment }}
                    </div>
                </header>

                <main>
                    <section class="hero">
                        <div class="eyebrow">Cloud-native application</div>
                        <h2>
                            Deploy with confidence.<br>
                            <span class="gradient-text">
                                Operate with visibility.
                            </span>
                        </h2>
                        <p>
                            A Flask application containerized with Docker
                            and orchestrated on Amazon EKS. This dashboard
                            helps demonstrate application health, version
                            changes, and progressive delivery.
                        </p>
                    </section>

                    <div class="section-heading">
                        <h3>Environment overview</h3>
                        <span>Live application information</span>
                    </div>

                    <section class="grid">
                        <article class="panel">
                            <div class="card-top">
                                <span class="card-label">Application status</span>
                                <div class="icon">✓</div>
                            </div>
                            <div class="metric green">Operational</div>
                            <div class="metric-note">
                                Application process is responding
                            </div>
                        </article>

                        <article class="panel">
                            <div class="card-top">
                                <span class="card-label">Release version</span>
                                <div class="icon">↗</div>
                            </div>
                            <div class="metric blue">{{ version }}</div>
                            <div class="metric-note">
                                Build identity supplied by environment
                            </div>
                        </article>

                        <article class="panel">
                            <div class="card-top">
                                <span class="card-label">Runtime platform</span>
                                <div class="icon">⌘</div>
                            </div>
                            <div class="metric purple">Amazon EKS</div>
                            <div class="metric-note">
                                Kubernetes container orchestration
                            </div>
                        </article>
                    </section>

                    <section class="panel time-panel">
                        <div>
                            <h3>Server clock</h3>
                            <p>
                                Coordinated Universal Time (UTC).<br>
                                Updates automatically in your browser.
                            </p>
                        </div>
                        <div class="clock" id="clock">{{ current_time }}</div>
                    </section>

                    <section class="panel deployment">
                        <h3>Deployment details</h3>
                        <div class="details">
                            <div>
                                <div class="detail-label">Environment</div>
                                <div class="detail-value">{{ environment }}</div>
                            </div>
                            <div>
                                <div class="detail-label">Framework</div>
                                <div class="detail-value">Python · Flask</div>
                            </div>
                            <div>
                                <div class="detail-label">Delivery strategy</div>
                                <div class="detail-value">
                                    Blue-green / Canary ready
                                </div>
                            </div>
                        </div>
                    </section>

                    <section class="panel deployment">
                        <h3>Technology stack</h3>
                        <div class="stack">
                            <span class="tag">Python</span>
                            <span class="tag">Flask</span>
                            <span class="tag">Docker</span>
                            <span class="tag">Amazon ECR</span>
                            <span class="tag">Amazon EKS</span>
                            <span class="tag">Argo CD</span>
                            <span class="tag">Argo Rollouts</span>
                            <span class="tag">GitOps</span>
                        </div>
                    </section>
                </main>

                <footer>
                    <span>CloudDeploy · Cloud Deployment Lab</span>
                    <span>{{ version }} · {{ environment }}</span>
                </footer>
            </div>

            <script>
                function updateClock() {
                    const now = new Date();
                    document.getElementById("clock").textContent =
                        now.toISOString().slice(11, 19) + " UTC";
                }

                updateClock();
                setInterval(updateClock, 1000);
            </script>
        </body>
        </html>
        """,
        app_name=APP_NAME,
        version=APP_VERSION,
        environment=APP_ENV,
        current_time=current_time,
    )


@app.route("/health")
def health():
    # Preserve the exact response expected by the existing unit test.
    return {"status": "healthy"}


@app.route("/ready")
def ready():
    return jsonify({"status": "ready"}), 200


@app.route("/version")
def version():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": APP_ENV,
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
