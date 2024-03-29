import argparse
from flask import Flask, render_template, request
from database import Database



def main():
    
    parser = argparse.ArgumentParser(
        description="Bandcamp release email visualizer"
    )
    parser.add_argument(
        '-i',
        '--input',
        help="Specify an input .mbox file to extract Bandcamp emails"
            "Default=None, application will access available database.json file",
        type=str,
        default=None
    )    
    args = parser.parse_args()

    database = Database(args.input)
   
    overall = database.length

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
