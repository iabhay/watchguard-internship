from pwinput import pwinput

import admin.admin_point
from admin.questioncontroller import Question
from database.module_queries.users_db import UsersDB
from database.module_queries.question_db import QuestionsDB
from database.module_queries.scores_db import ScoresDB
from admin.usercontroller import User
from config.config import Config
from admin.usercontroller import User


class AdminController(User):
    def __init__(self):
            super().__init__()
            self.ques = Question()

    def create_user(self):
        User.add_user(role="player", is_changed=0)

    def update_user_password(self):
        username = input("Enter Username: ")
        new_password = pwinput(Config.SECURE_PASSWORD_PROMPT,"*")
        self.userdb.update_user_password_by_admin(username, new_password)

    def show_all_admins(self):
        self.userdb.read_all_admin()

    def show_all_loggedin(self):
        self.score.show_all_loggedin()

    def delete_user(self):
        username = input("Enter username to delete: ")
        self.userdb.delete_user_by_admin(username, "player")

    def add_question(self):
        self.ques.add_question()

    def show_question(self):
        try:
            total_ques = self.quesdb.count_questions()
            ques_id = int(input(f"Enter Question ID to show details: "))
            self.ques.show_question_by_id(ques_id)
        except Exception:
            print(Exception.__name__)
            print("Show Question from admin failed!!")
    def show_all_questions(self):
        self.ques.show_all_questions()

    def update_question(self):
        try:
            ques_id = int(input(f"Enter Question ID to update details: "))
            self.ques.update_question_by_id(ques_id)
        except Exception:
            print(Exception.__name__)
            print("Update Question from admin failed!!")

    def delete_question(self):
        # try:
            total_ques = self.quesdb.count_questions()
            ques_id = int(input(f"Enter Question ID to delete details: "))
            self.ques.delete_question_by_id(ques_id)
        # except Exception as e:
        #     print(Exception.__name__)
        #     print("Delete Question from admin failed!!", e)