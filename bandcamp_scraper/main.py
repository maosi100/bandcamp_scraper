from argparse import ArgumentParser, Namespace
from flask import Flask, render_template, request

from email_scraper import EmailScraper
from database_handler import DatabaseHandler

def extract_args() -> Namespace:
    parser = ArgumentParser(
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

    return parser.parse_args()

def main() -> None:
    args = extract_args()
    
    if args.input:
        email_scraper = EmailScraper()
        email_scraper.process(args.input)

    database = DatabaseHandler()

    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "GET":
            release, count = database.get_next_release()
            
            if release:
                return render_template(
                    "home.html",
                    release=release,
                    count=count,
                    overall=database.length
                )
            else:
                return render_template("exceeded.html")

        if request.method == "POST":
            database.reset_processing_flag()
            release, count = database.get_next_release()
            
            if release:
                return render_template(
                    "home.html",
                    release=release,
                    count=count,
                    overall=database.length
                )
            else:
                return render_template("exceeded.html")

    @app.route("/leave")
    def leave():
        database.save_state()
        return render_template("leave.html")
    app.run(host="0.0.0.0", port=8000, debug=True)


if __name__ == "__main__":
    main()
