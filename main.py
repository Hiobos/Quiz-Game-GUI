from question_model import Question
from data import Questions_data
from quiz_brain import QuizBrain

question_bank = []
questions = Questions_data()

for question in questions.add_questions():
    new_question = Question(question['question'], question['correct_answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.more_questions(question_bank):
    quiz.next_question()



