import random
from database.module_queries.users_db import UsersDB
from database.module_queries.scores_db import ScoresDB
from database.module_queries.question_db import QuestionsDB
from config.config import Config

class Player:
    def __init__(self):
        self.user = UsersDB()
        self.score = ScoresDB()
        self.ques = QuestionsDB()

    def playermodule(self, username):
        print(f"You are logged in successfully.")
        ask = int(input(Config.PLAYER_PROMPT))
        if ask == 4:
            print("Exiting login Menu.!!")
        while ask != 4:
            ask = int(input(Config.PLAYER_PROMPT))
            if ask == 1:
                self.playgame(username)
            elif ask == 2:
                self.highscoreinfo(username)
            elif ask == 3:
                self.leaderboard()
            elif ask == 4:
                print(f"Exiting Player Menu!!")
                break
            else:
                print("Please Select Carefully!")
                ask = int(input(Config.PLAYER_PROMPT))

    def playgame(self, username):
        print("We will give you 10 Questions.")
        print("Here your game starts...")
        userscore = 0
        for i in range(0, 10):
            userscore += self.question()
        print(f"You scored {userscore} out of 10.")
        self.highscorer(username, userscore)

    def highscorer(self, name, score):
        entry = self.score.fetch_player_score(name)
        if entry < score:
            self.score.update_player_score(name, score)
            print("Updated your high score.")

    def highscoreinfo(self, name):
        self.score.show_player_score(name)

    def leaderboard(self):
        self.score.show_leaderboard()

    def question(self):
        # total_ques = self.ques.count_questions()
        # if total_ques == 0:
        #     print("No Questions in database!!")
        #     return 0
        current_score = 0
        # rand_num = random.randint(0, total_ques)
        curr_content = self.ques.get_question()
        print(f"Question: {curr_content[1]}")
        print(f"Options: ")
        my_options = [curr_content[2], curr_content[3], curr_content[4], curr_content[5]]
        correct_option_ind = curr_content[6]
        option_dict = {
            "A": 1,
            "B": 2,
            "C":3,
            "D":4
        }
        correct_option = curr_content[option_dict[correct_option_ind]]
        random.shuffle(my_options)
        for i in range(0, 4):
            print(f"{i + 1}. {my_options[i]}")
        ask_option = int(input("Write correct option (1,2,3,4) : "))
        while ask_option <= 0 or ask_option >= 5:
            print("Please Select Carefully.")
            ask_option = int(input("Write correct option (1,2,3,4) : "))
        if my_options[ask_option-1] == correct_option:
            current_score += 1
        return current_score

