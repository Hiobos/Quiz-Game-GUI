import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.list_length = 0
        self.current_question = None

    def more_questions(self, q_list):
        self.list_length = len(q_list)
        return self.question_number != self.list_length

    def return_score(self):
        return self.score

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1

        full_question = f"Q.{self.question_number}: {html.unescape(self.current_question.text)} (true/false): "
        return full_question
        #self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer):
        if user_answer.lower() == self.current_question.answer.lower():
            self.score += 1
            print(f"You're right, SCORE: {self.score}/{self.question_number}.")
            print('\n')
        else:
            print(f"Incorrect answer, SCORE: {self.score}/{self.question_number}.")
            print('\n')
        if self.question_number == self.list_length:
            print(f"You're final score is {self.score}/{self.question_number} !")