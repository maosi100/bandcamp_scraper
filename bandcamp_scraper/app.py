from flask import Flask, render_template

def run_flask():
    app = Flask(__name__)   

    @app.route("/")
    
    def home():
        return render_template("home.html") 

    app.run(host="0.0.0.0", port=8000, debug=True)
