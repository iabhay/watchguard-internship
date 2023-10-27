from datetime import datetime
from tabulate import tabulate
from database.databaseconnection import DatabaseConnection
from database.database_query import UsersTableQuery, ScoresTableQuery, QUESTIONSTableQuery
from utils.Exception_Handler.sql_exception_handler import exception_handler
from config.config import Config
QUIZ = "QUIZ.db"

class UsersDB:

    def __init__(self):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            cursor.execute(UsersTableQuery.query_create_user)
            cursor.execute(ScoresTableQuery.query_create_score)
            cursor.execute(QUESTIONSTableQuery.query_create_question)
            cursor.close()

    def create_user(self, username, password, role, is_changed=1):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            cursor.execute(UsersTableQuery.query_insert_user, (username, password, role, is_changed))
            tm = datetime.now()
            dt_string = tm.strftime("%d/%m/%Y %H:%M:%S")
            cursor.execute(ScoresTableQuery.query_insert_score, (dt_string, username, 0, 0))
            cursor.close()


    def delete_user(self, username, password):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            cursor.execute(UsersTableQuery.query_delete_user, (username, password))
            cursor.execute(ScoresTableQuery.query_delete_score, (username,))
            cursor.close()


    def delete_user_by_admin(self, username, role):
        #check if admin
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            cursor.execute(UsersTableQuery.query_delete_user_by_admin, (username,role))
            cursor.execute(ScoresTableQuery.query_delete_score, (username,))
            cursor.close()


    def read_all_admin(self):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            table = cursor.execute(UsersTableQuery.query_select_all_admin).fetchall()
            print(tabulate(table))
            cursor.close()


    def update_admin_to_player(self, username):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            cursor.execute(UsersTableQuery.query_update_role, ("player", username))
            cursor.close()


    def update_player_to_admin(self, username):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            cursor.execute(UsersTableQuery.query_update_role, ("admin", username))
            cursor.close()


    def check_user(self, username):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            count = cursor.execute(UsersTableQuery.query_check_existence, (username, )).fetchone()
            cursor.close()
            if not count:
                return False
            return True


    def update_user_password(self, username, password, new_password):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            cursor.execute(UsersTableQuery.query_update_pasword, (new_password, username, password))
            cursor.close()


    def update_user_password_by_admin(self, username, new_password):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            cursor.execute(UsersTableQuery.query_update_pasword_by_admin, (new_password, username))
            cursor.close()


    def check_login(self, username, password):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            res = cursor.execute(UsersTableQuery.query_select_user, (username, password)).fetchone()
            cursor.close()
            if not res:
                return None
            return res

