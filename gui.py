import tkinter as tk
import json
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("🧠 Python Quiz")
        self.master.geometry("500x350")
        self.master.resizable(False, False)

        self.question_index = 0
        self.score = 0

        self.load_questions()
        self.create_widgets()
        self.show_question()

    def load_questions(self):
        try:
            with open("questions.json", "r", encoding="utf-8") as f:
                self.questions = json.load(f)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load questions: {e}")
            self.master.quit()

    def create_widgets(self):
        self.question_label = tk.Label(self.master, text="", wraplength=400, font=("Arial", 14), pady=20)
        self.question_label.pack()

        self.option_buttons = []
        for key in ["A", "B", "C", "D"]:
            btn = tk.Button(self.master, text="", width=40, font=("Arial", 12),
                            command=lambda k=key: self.check_answer(k))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

    def show_question(self):
        if self.question_index < len(self.questions):
            q = self.questions[self.question_index]
            self.question_label.config(text=f"Q{self.question_index + 1}: {q['question']}")

            for i, key in enumerate(["A", "B", "C", "D"]):
                self.option_buttons[i].config(text=f"{key}. {q['options'][key]}")
        else:
            self.show_result()

    def check_answer(self, selected_option):
        correct = self.questions[self.question_index]["answer"]
        if selected_option == correct:
            self.score += 1

        self.question_index += 1
        self.show_question()

    def show_result(self):
        percentage = (self.score / len(self.questions)) * 100
        msg = f"✅ Score: {self.score} / {len(self.questions)}\n🧮 Percentage: {percentage:.1f}%"

        if percentage == 100:
            msg += "\n🎉 Perfect score!"
        elif percentage >= 70:
            msg += "\n👍 Great job!"
        else:
            msg += "\n📘 Keep practicing!"

        messagebox.showinfo("Quiz Completed", msg)
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
