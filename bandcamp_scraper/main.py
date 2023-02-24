from sys import exit
from email_scraper import create_database
import json
from flask import Flask, render_template

def find_database():
    try:
        with open("./database.json", "r") as file:
            database_json = json.load(file)
            return database_json
    except FileNotFoundError:
        return False

def validate_mbox(path):
    if "mbox" not in path[:-4]:
        return False
    return True

def get_release(database): 
    for item in database:
        if item[2] == "0":
            item[2] = "1"
            return item[1]

def main():
 
    database = find_database()

    if not database:
        mbox_path = input("Please enter path to valid .mbox file: ")
        if not validate_mbox(mbox_path):
            exit("Please enter valid mbox file")
        if not create_database(mbox_path):
            exit("Could not create database")
        database = find_database()
    
    app = Flask(__name__)

    @app.route("/")
    def home():
        release = get_release(database)
        return render_template("home.html", release=release)

    app.run(host="0.0.0.0", port=8000, debug=True)


if __name__ == "__main__":
    main()
