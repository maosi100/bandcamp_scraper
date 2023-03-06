from email_scraper import create_database
import json
from flask import Flask, render_template, request

# Retrieve database file
def retrieve_database():
    while True:
        mbox_path = input("Please enter path to valid .mbox file: ")
        if not validate_mbox(mbox_path):
            print ("File invalid, try again.")
        else:
            break
    if not create_database(mbox_path):
        exit("Could not create database")

# Open database
def open_database():
    try:
        with open("./database.json", "r") as file:
            database_json = json.load(file)
            return database_json
    except FileNotFoundError:
        return False

# Check for correct path
def validate_mbox(path):
    if "mbox" not in path[:-4]:
        return False
    return True

# Get latest release from database
def get_release(database): 
    for item in database:
        if item["Flag"] == "0":
            item["Flag"] = "1"
            return item["Url"], item["Count"]
    return False

# Save changes to database file
def save_state(database):
    try:
        with open("./database.json", "w") as file:
            database = json.dumps(database, indent=4)
            file.write(database)
            return True
    except FileNotFoundError:
        return False

# Get the item count of database
def count_items(database):
    return database[-1]["Count"]

# Set back database by two
def set_back(database):
    for item in database:
        if item["Flag"] == "0":
            count = item["Count"] - 1
            database[(count - 1)]["Flag"] = "0"
            database[(count - 2)]["Flag"] = "0"
            return True


def main():
    # Access the release database
    database = open_database()
    if not database:
        retrieve_database()
        database = open_database()
   
    overall = count_items(database)

    # Start Flask for application front end
    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "GET":
            return_values = get_release(database)
            release = return_values[0]
            count = return_values[1]
            
            if release:
                return render_template("home.html", release=release, count=count, overall=overall)
            else:
                return render_template("exceeded.html")

        if request.method == "POST":
            set_back(database)
            return_values = get_release(database)
            release = return_values[0]
            count = return_values[1]
            
            if release:
                return render_template("home.html", release=release, count=count, overall=overall)
            else:
                return render_template("exceeded.html")

    @app.route("/leave")
    def leave():
        save_state(database)
        return render_template("leave.html")

    app.run(host="0.0.0.0", port=8000, debug=True)


if __name__ == "__main__":
    main()
