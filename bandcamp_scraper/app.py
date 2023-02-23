from flask import render_template
import connexion
from releases import oldest_release


app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route("/")
def home():
    release = oldest_release()
    return render_template("home.html", release=release)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
