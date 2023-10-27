import hashlib
from pwinput import pwinput
from database.module_queries.users_db import UsersDB
from database.module_queries.scores_db import ScoresDB
from database.module_queries.question_db import QuestionsDB
from config.config import Config
from utils.password_validator import password_validation

class Register:
    def __init__(self):
        self.user = UsersDB()
        self.ques = QuestionsDB()
        self.score = ScoresDB()

    def register_module(self, role="player"):
        username = input("Enter username: ")
        if not self.check_registration(username):
            print(Config.SECURE_PASSWORD_PROMPT)
            password = pwinput("Enter Password: ", mask="*")
            if not password_validation(password):
                print("Invalid Password!!")
            else:
                hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                try:
                    self.user.create_user(username, hashed_password, role)
                    print("Registered successfully!!")
                except Exception:
                    print(Exception.__name__)
                    print("Data not registered successfully.")

    def check_registration(self, name):
        try:
            is_already_registered = self.user.check_user(name)
            if is_already_registered:
                print("Already registered!!\nTry login!!")
                return True
            else:
                return False
        except Exception:
            print(Exception.__name__)
            print("Checking user failed.!")
