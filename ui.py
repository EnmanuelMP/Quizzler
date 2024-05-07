from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain) -> None:
        self.quiz = quiz_brain

    #Setting components
        #scr
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #label
        self.lbl_score = Label(text="Score: 0", bg=THEME_COLOR, fg="White")

        #canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.lbl_question = self.canvas.create_text(150, 125, text="Question", font=("Arial",20,"italic"), width=280)

        #buttons
        img_true = PhotoImage(file="./images/true.png")
        img_false = PhotoImage(file="./images/false.png")
        self.btn_true = Button(image=img_true, highlightthickness=0, command=self.true_pressed)
        self.btn_false = Button(image=img_false, highlightthickness=0, command=self.false_pressed)

    #Locating components in scr
        self.lbl_score.grid(row=0, column=2)
        self.canvas.grid(row=1, column=1, columnspan=2, pady=50)
        self.btn_true.grid(row=2,column=1)
        self.btn_false.grid(row=2, column=2)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="White")

        if self.quiz.still_has_questions():
            self.lbl_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.lbl_question, text=q_text)

        else:
            self.canvas.itemconfig(self.lbl_question, text=f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        
        self.window.after(1000, self.get_next_question)




