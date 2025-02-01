from tkinter import*
from  question_model import Question
import html

THEME_COLOR = "#375362"

class QuizWindow():
    def __init__(self,q_list):
        self.window=Tk()
        self.window.title("Quizziler Game")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score=0
        self.question_list=q_list
        self.question_number=0
        self.current_question=None

        self.score_label = Label(text=f"Score:{self.score}")
        self.score_label.grid(row=0, column=1)

        self.que = Canvas(width=300, height=250)
        self.question=self.que.create_text(150,125,text="",font=("Arial", 20, "italic"))

        self.que.grid(row=1, column=0, columnspan=2)

        true = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=true, width=97, height=100)
        self.correct_button.grid(row=2, column=0)

        false = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=false, width=97, height=100)
        self.wrong_button.grid(row=2, column=1)

        self.canvas_update()

        self.window.mainloop()


    def canvas_update(self):

        if self.question_number < len(self.question_list):

            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            q_text = html.unescape(self.current_question.text)
            self.que.itemconfig(self.question,text=q_text)
