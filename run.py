from trivia import sport_questions


# Question class
class Question:
    """
    Create and initialise objects for the questions class.
    """

    def __init__(self, the_question, correct_answer):
        self.question = the_question
        self.answer = correct_answer


# first_question = Question("What's your name?", "True")
# print(first_question.question)


# 3. Class that prints and runs the questions
class TriviaFunction:
    def __init__(self, list):
        self.number_of_question = 0
        self.list_of_questions = list

    def next_question(self):
        """
        Retrieves question number from the list. Inputs the question and asks user for the answer.
        """
        current_q = self.list_of_questions[self.number_of_question]
        self.number_of_question += 1
        input(
            f"Question {self.number_of_question}: {current_q.question}(Select letter):\n  "
        )

    def is_questions_remaining(self):
        """
        Checks if there are still remaining questions in the trivia.
        """
        if self.number_of_question < len(self.list_of_questions):
            return True
        else:
            False


array_of_questions = []
"""
The for loop will go over the questions in the database in trivia.py. For each question an object will be created and appended to the array of questions.
"""
for question in sport_questions:
    question_1 = question[0]["question"]
    question_correct_answer = question[0]["correct_answer"]
    add_question = Question(question_1, question_correct_answer)
    array_of_questions.append(add_question)

# print(array_of_questions)
trivia = TriviaFunction(array_of_questions)

while trivia.is_questions_remaining():
trivia.next_question()
