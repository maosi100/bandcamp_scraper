from flask import Flask, render_template
from main import get_release

def run_flask():
    app = Flask(__name__)   

    @app.route("/")
    def home():
        release = get_release() 
        return render_template("home.html", release=release)

    app.run(host="0.0.0.0", port=8000, debug=True)
