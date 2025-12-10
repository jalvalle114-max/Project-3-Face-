import pickle
import os

DB_PATH = "face_database.pkl"

def save_database(people):
    with open(DB_PATH, "wb") as f:
        pickle.dump(people, f)

def load_database():
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "rb") as f:
            return pickle.load(f)
    return None
