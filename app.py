from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static")
app.jinja_env.cache = {}

@app.after_request
def no_cache(resp):
    resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    resp.headers["Pragma"] = "no-cache"
    resp.headers["Expires"] = "0"
    return resp

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/.well-known/<path:_sub>")
def well_known(_sub):
    return ("", 204)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)


