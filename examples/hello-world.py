from flask import Flask
from flask import render_template_string

app = Flask(__name__)

@app.route("/")
def hello_world():
    html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Hello</title>
<style>
  :root { --bg: #f5f7fb; --card: #ffffff; --accent: #2563eb; --muted: #6b7280; }
  body {
    margin: 0;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(180deg, var(--bg), #e9eef8);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    color: #111827;
  }
  .card {
    background: var(--card);
    padding: 36px;
    max-width: 720px;
    width: calc(100% - 48px);
    box-shadow: 0 10px 30px rgba(2,6,23,0.08);
    border-radius: 12px;
    border: 1px solid rgba(15,23,42,0.04);
    text-align: center;
  }
  h1 { margin: 0 0 8px; color: var(--accent); font-size: 2.25rem; }
  p { margin: 0; color: var(--muted); }
</style>
</head>
<body>
  <div class="card" role="main">
    <h1>Hello World!!!</h1>
    <p>Welcome 🚀 — This is a simple Flask app ⚙️ by Anirban 😊 </p>
  </div>
</body>
</html>"""
    return render_template_string(html)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=9000)
