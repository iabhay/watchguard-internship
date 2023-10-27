from database.databaseconnection import DatabaseConnection
from database.module_queries.question_db import QuestionsDB
import json
questions_data = "database/questions.json"
QUIZ = "QUIZ.db"
ques = QuestionsDB()
with open(questions_data, "r") as file:
    content = json.load(file)
    with DatabaseConnection(QUIZ) as connection:
        cursor = connection.cursor()
        for item in content:
            print(item["id"])
            ques.add_question(item["id"], item["question"], item["A"], item["B"], item["C"], item["D"], item["answer"])
