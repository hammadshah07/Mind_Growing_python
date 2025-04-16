import tkinter as tk
import random

# Motivational Quotes
quotes = [
    "Your only limit is your mind.",
    "Stay positive, work hard, make it happen.",
    "Challenges make life interesting.",
    "Every day is a chance to grow."
]

# Memory Challenge Words
memory_words = ["Apple", "Mountain", "River", "Elephant", "Piano"]

def show_memory_challenge():
    word = random.choice(memory_words)
    challenge_label.config(text=f"Remember this word: {word}")
    root.after(3000, lambda: challenge_label.config(text="What was the word?"))

def show_math_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    challenge_label.config(text=f"What is {num1} + {num2}?")
    math_answer.set(num1 + num2)

def check_answer():
    if answer_entry.get().isdigit() and int(answer_entry.get()) == math_answer.get():
        challenge_label.config(text="Correct!")
    else:
        challenge_label.config(text="Try Again!")

def show_quote():
    quote_label.config(text=random.choice(quotes))

# GUI Setup
root = tk.Tk()
root.title("Mind Growth App")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

challenge_label = tk.Label(frame, text="Welcome! Choose an activity.")
challenge_label.grid(row=0, columnspan=2)

memory_button = tk.Button(frame, text="Memory Challenge", command=show_memory_challenge)
memory_button.grid(row=1, column=0)

math_button = tk.Button(frame, text="Math Challenge", command=show_math_problem)
math_button.grid(row=1, column=1)

math_answer = tk.IntVar()
answer_entry = tk.Entry(frame)
answer_entry.grid(row=2, columnspan=2)

check_button = tk.Button(frame, text="Check Answer", command=check_answer)
check_button.grid(row=3, columnspan=2)

quote_button = tk.Button(frame, text="Motivational Quote", command=show_quote)
quote_button.grid(row=4, columnspan=2)

quote_label = tk.Label(frame, text="")
quote_label.grid(row=5, columnspan=2)

root.mainloop()
