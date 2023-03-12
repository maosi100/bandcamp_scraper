from flask import Flask, render_template, request
from database import Database

def main():
    # Access the release database
    database = Database("/Users/maximosipovs/Downloads/alte mailbox/Bandcamp all.mbox/mbox")
   
    overall = database.length

    # Start Flask for application front end
    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "GET":
            return_values = database.get_release()
            release = return_values[0]
            count = return_values[1]
            
            if release:
                return render_template("home.html", release=release, count=count, overall=overall)
            else:
                return render_template("exceeded.html")

        if request.method == "POST":
            database.set_back()
            return_values = database.get_release()
            release = return_values[0]
            count = return_values[1]
            
            if release:
                return render_template("home.html", release=release, count=count, overall=overall)
            else:
                return render_template("exceeded.html")

    @app.route("/leave")
    def leave():
        database.save_state()
        return render_template("leave.html")

    app.run(host="0.0.0.0", port=8000, debug=True)


if __name__ == "__main__":
    main()
