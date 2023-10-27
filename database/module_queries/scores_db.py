from datetime import datetime
from tabulate import tabulate
from database.databaseconnection import DatabaseConnection
from database.database_query import UsersTableQuery, ScoresTableQuery, QUESTIONSTableQuery
from utils.Exception_Handler.sql_exception_handler import exception_handler
from config.config import Config
from config.config import Config
QUIZ = "QUIZ.db"


class ScoresDB:
    def __init__(self):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            cursor.execute(UsersTableQuery.query_create_user)
            cursor.execute(ScoresTableQuery.query_create_score)
            cursor.execute(QUESTIONSTableQuery.query_create_question)
            cursor.close()

    def update_player_score(self, username, highscore):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            tm = datetime.now()
            dt_string = tm.strftime("%d/%m/%Y %H:%M:%S")
            cursor.execute(ScoresTableQuery.query_update_score, (dt_string, highscore, username))
            cursor.close()

    def show_leaderboard(self):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            table = cursor.execute(ScoresTableQuery.query_leaderboard).fetchall()
            print(tabulate(table))
            cursor.close()

    def show_player_score(self, username):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            player_score = cursor.execute(ScoresTableQuery.query_select_userscore, (username, )).fetchone()
            print(f"Last Played: {player_score[0]}\nUser: {player_score[1]}\nRole: {player_score[2]}\nHighscore: {player_score[3]}\n"
                  f"Login Status: {'Active' if player_score[4] == 1 else 'Not-Active'}")
            cursor.close()

    def fetch_player_score(self, username):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            player_score = cursor.execute(ScoresTableQuery.query_fetch_score, (username, )).fetchone()
            cursor.close()
            return player_score[0]

    def mark_login(self, username):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            cursor.execute(ScoresTableQuery.query_update_login_status, (1, username))
            cursor.close()

    def mark_logout(self, username):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            cursor.execute(ScoresTableQuery.query_update_login_status, (0, username))
            cursor.close()


    def check_login(self, username, password):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            entry = cursor.execute(ScoresTableQuery.query_select_user, (username, password)).fetchone()
            cursor.close()
            return entry


    def show_all_user(self):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            table = cursor.execute(ScoresTableQuery.query_select_all_user)
            print(tabulate(table))
            cursor.close()


    def show_all_loggedin(self):
        with DatabaseConnection(QUIZ) as connection:
            cursor = connection.cursor()
            table = cursor.execute(ScoresTableQuery.query_select_all_loggedin, (1,))
            print(tabulate(table))
            cursor.close()
