from pwinput import pwinput
from database.module_queries.users_db import UsersDB
from database.module_queries.question_db import QuestionsDB
from database.module_queries.scores_db import ScoresDB
# from admin.admin import AdminController
from admin.usercontroller import User
from config.config import Config
from admin.admincontroller import AdminController


class SuperAdminController(AdminController):
    def __init__(self):
        super().__init__()
        # print('here')
        self.user = User()
        # self.userdb = UsersDB()
        # self.score = ScoresDB()
        # self.ques = QuestionsDB()
        # self.admin = AdminController()

    def create_new_admin(self):
        try:
            self.user.add_user("admin", 0)
            print(f"admin added successfully.")
        except Exception:
            print(Exception.__name__)
            print("admin not created by superadmin!!")

    # def create_new_user(self):
    #     self.admin.add_user()

    def change_admin_to_user(self):
        username = input("Enter Username to change role: ")
        try:
            self.userdb.update_admin_to_player(username)
            print("Role Changed Successfully.")
        except:
            print("Not Found!!")

    def change_user_to_admin(self):
        username = input("Enter Username to change role: ")
        try:
            self.userdb.update_player_to_admin(username)
            print("Role Changed Successfully.")
        except:
            print("Not Found!!")
            
    # def show_user(self):
    #     self.admin.show_user()
    #
    # def show_all_user(self):
    #     self.admin.show_all_users()
    #
    # def show_leaderboard(self):
    #     self.admin.show_leaderboard()

    def show_all_loggedin(self):
        self.score.show_all_loggedin()

    # def show_all_admins(self):
    #     self.admin.show_all_admins()
    #
    # def add_question(self):
    #     self.admin.add_question()
    #
    # def update_question(self):
    #     self.admin.update_question()
    #
    # def show_question(self):
    #     self.admin.show_question()
    #
    # def show_all_questions(self):
    #     self.admin.show_all_questions()
    #
    # def delete_question(self):
    #     self.admin.delete_question()

    def delete_admin(self):
        try:
            username = input("Enter username: ")
            entry = self.userdb.check_user(username)
            if not entry:
                print("User not found!!")
            else:
                confirmation = input("Are you sure? (Yes/No)\n=>")
                if confirmation == "yes":
                    self.userdb.delete_admin_by_superadmin(username)
                    print(f"{username}, deleted successfully!!")
        except Exception:
            print(Exception.__name__)
            print("admin deletion from superadmin failed!!")
