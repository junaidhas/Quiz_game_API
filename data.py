# question_data =  [
#         {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#          "question": "Nutella is produced by the German company Ferrero.", "correct_answer": "False",
#          "incorrect_answers": ["True"]}, {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#                                           "question": "A scientific study on peanuts in bars found traces of over 100 unique specimens of urine.",
#                                           "correct_answer": "False", "incorrect_answers": ["True"]},
#         {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#          "question": "The Sun rises from the North.", "correct_answer": "False", "incorrect_answers": ["True"]},
#         {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#          "question": "The color orange is named after the fruit.", "correct_answer": "True",
#          "incorrect_answers": ["False"]},
#         {"category": "General Knowledge", "type": "boolean", "difficulty": "easy", "question": "Pluto is a planet.",
#          "correct_answer": "False", "incorrect_answers": ["True"]},
#         {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#          "question": "The Lego Group was founded in 1932.", "correct_answer": "True", "incorrect_answers": ["False"]},
#         {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#          "question": "Scotland voted to become an independent country during the referendum from September 2014.",
#          "correct_answer": "False", "incorrect_answers": ["True"]},
#         {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#          "question": "The National Animal of Scotland is the Unicorn.", "correct_answer": "True",
#          "incorrect_answers": ["False"]}, {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#                                            "question": "Vietnam&#039;s national flag is a red star in front of a yellow background.",
#                                            "correct_answer": "False", "incorrect_answers": ["True"]},
#         {"category": "General Knowledge",
#          "type": "boolean",
#          "difficulty": "easy",
#          "question": "Jingle Bells was originally meant for Thanksgiving",
#          "correct_answer": "True",
#          "incorrect_answers": ["False"]}
# ]

import requests

paramters = {
    "amount":10,
    "type":"boolean",
}

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean",params=paramters)
response.raise_for_status()
data =response.json()
question_data = data["results"]
print(question_data)
