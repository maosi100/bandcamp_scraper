from sys import exit
from email_scraper import create_database
from app import run_flask

def find_database():
    try:
        with open("./database.json", "r") as file:
            return file
    except FileNotFoundError:
        return False

def validate_mbox(path):
    if "mbox" not in path[:-4]:
        return False
    return True


def main():
 
    database = find_database()

    if not database:
        mbox_path = input("Please enter path to valid .mbox file: ")
        if not validate_mbox(mbox_path):
            exit("Please enter valid mbox file")
        database = create_database(mbox_path)
        if not database:
            exit("Could not create database")
    
    run_flask()


if __name__ == "__main__":
    main()

