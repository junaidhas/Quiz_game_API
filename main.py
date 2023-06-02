# class User:
#     def __init__(self,user_id,username):
#         print("New user is being created")
#         self.id=user_id
#         self.name=username
#         self.followers=0
#
#
#
# user_1 = User("001","Junaid")
#
# print(user_1.name)
# print(user_1.id)
# print(user_1.name)
#
#
# user_2 = User("002","Hasan")
# print(user_2.name)
# print(user_2.id)
# print(user_2.followers)

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)

    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)
# while quiz.still_has_questions():
#     quiz.next_question()

print("your quiz has ended")
print(f"Your final score was {quiz.score}/{quiz.question_number}")

