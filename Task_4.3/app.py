from flask import Flask, render_template_string
import os
import socket

app = Flask(__name__)

APP_ENV = os.environ.get("APP_ENV", "development")
PORT = int(os.environ.get("PORT", 5000))
APP_TITLE = os.environ.get("APP_TITLE", "Docker Distinction Demo")

PAGE = """
<!DOCTYPE html>
<html>
<head><title>{{ title }}</title></head>
<body style="font-family: sans-serif; text-align: center; margin-top: 10%;">
    <h1>{{ title }}</h1>
    <p>Environment: <strong>{{ env }}</strong></p>
    <p>Container hostname: <strong>{{ hostname }}</strong></p>
    <p>This page is served from a Docker container, publicly accessible over HTTP.</p>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        PAGE, title=APP_TITLE, env=APP_ENV, hostname=socket.gethostname()
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
