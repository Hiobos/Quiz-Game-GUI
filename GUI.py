from tkinter import *
from question_model import Question
from data import Questions_data
from quiz_brain import QuizBrain
import time

class GraphicInterface:
    def __init__(self):
        window = Tk()
        window.title('Quiz Game')
        window.minsize(500, 500)
        window.maxsize(500, 500)
        window.config(bg='#e6b55c', pady=5, padx=30)
        #---gets questions into a list
        self.question_bank = []
        questions = Questions_data()
        time.sleep(1)

        for question in questions.add_questions():
            new_question = Question(question['question'], question['correct_answer'])
            self.question_bank.append(new_question)

        self.quiz = QuizBrain(self.question_bank)

        #Text variables
        self.canvas = Canvas(window, width=440, height=300, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.score_text = StringVar(window, f"Score: {self.quiz.return_score()}")

        #Defining UI elements
        score_label = Label(window, textvariable=self.score_text, font=("Arial", 14), bg='#e6b55c')
        self.question_text_id = self.canvas.create_text(
            220, 150,
            text=self.quiz.next_question(),
            font=("Arial", 16),
            width=400,
            fill="black"
        )
        right_button = Button(text="V")
        wrong_button = Button(text="X")

        def disable_buttons():
            right_button.config(state=DISABLED)
            wrong_button.config(state=DISABLED)

        def button_check(user_answer):
            if self.quiz.more_questions(self.question_bank):
                self.quiz.check_answer(user_answer)
                self.canvas.itemconfig(self.question_text_id, text=self.quiz.next_question())
                self.score_text.set(f"Score: {self.quiz.return_score()}")
            else:
                self.quiz.check_answer(user_answer)
                self.canvas.itemconfig(self.question_text_id, text=f"Final Score: {self.quiz.return_score()}/10")
                self.score_text.set(f"")
                disable_buttons()

        #Configuring labels and buttons
        score_label.config(bg='#e6b55c')
        right_button.config(bg='green', padx=25, pady=20, command=lambda: button_check('true'))
        wrong_button.config(bg='red', padx=25, pady=20, command=lambda: button_check('false'))

        #Placement of elements on UI
        score_label.grid(row=0, column=0, columnspan=2)
        right_button.grid(row=2, column=0)
        wrong_button.grid(row=2, column=1)

        #mainloop
        window.mainloop()