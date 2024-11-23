import tkinter as tk
from tkinter import messagebox

# Function to display message when the user completes a section
def show_message(title, message):
    messagebox.showinfo(title, message)

# Function to check quiz answers
def check_quiz_answer(answer, correct_answer):
    if answer == correct_answer:
        show_message("Correct!", "That's the right answer! Good job.")
    else:
        show_message("Incorrect", "That's not correct. Try again or review the material.")

# Main application window
root = tk.Tk()
root.title("Phishing Awareness Training")
root.geometry("600x400")

# Title label
title_label = tk.Label(root, text="Phishing Awareness Training", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Section buttons
def phishing_definition():
    messagebox.showinfo(
        "What is Phishing?",
        "Phishing is a type of cyberattack where attackers trick people into revealing sensitive information like passwords or credit card numbers."
    )

def recognizing_emails():
    info = (
        "How to Recognize Phishing Emails:\n"
        "- Suspicious sender addresses\n"
        "- Generic greetings like 'Dear Customer'\n"
        "- Urgent or threatening language\n"
        "- Links or attachments (hover to inspect links)"
    )
    messagebox.showinfo("Recognizing Phishing Emails", info)

def fake_websites():
    info = (
        "Spotting Fake Websites:\n"
        "- Look for 'https://' in the URL\n"
        "- Check for spelling errors or low-quality design\n"
        "- Be cautious of pop-ups asking for sensitive information"
    )
    messagebox.showinfo("Spotting Fake Websites", info)

def social_engineering():
    info = (
        "Understanding Social Engineering:\n"
        "- Attackers may pretend to be someone you trust, like IT or your boss.\n"
        "- They use fear, urgency, or rewards to manipulate you.\n"
        "- Always verify unusual requests via official channels."
    )
    messagebox.showinfo("Social Engineering Tactics", info)

# Buttons for each section
button1 = tk.Button(root, text="What is Phishing?", command=phishing_definition, bg="lightblue", width=30)
button1.pack(pady=5)

button2 = tk.Button(root, text="Recognizing Phishing Emails", command=recognizing_emails, bg="lightgreen", width=30)
button2.pack(pady=5)

button3 = tk.Button(root, text="Spotting Fake Websites", command=fake_websites, bg="lightcoral", width=30)
button3.pack(pady=5)

button4 = tk.Button(root, text="Social Engineering Tactics", command=social_engineering, bg="lightyellow", width=30)
button4.pack(pady=5)

# Quiz Section
quiz_label = tk.Label(root, text="Phishing Awareness Quiz", font=("Arial", 16, "bold"))
quiz_label.pack(pady=20)

quiz_question = tk.Label(root, text="Which of these is a sign of a phishing email?")
quiz_question.pack()

# Quiz options
quiz_answer = tk.StringVar()

quiz_option1 = tk.Radiobutton(root, text="Generic Greeting like 'Dear Customer'", variable=quiz_answer, value="1")
quiz_option2 = tk.Radiobutton(root, text="Personalized Greeting", variable=quiz_answer, value="2")
quiz_option3 = tk.Radiobutton(root, text="Email from a known address", variable=quiz_answer, value="3")

quiz_option1.pack(anchor="w")
quiz_option2.pack(anchor="w")
quiz_option3.pack(anchor="w")

def submit_quiz():
    check_quiz_answer(quiz_answer.get(), "1")

quiz_submit_button = tk.Button(root, text="Submit Answer", command=submit_quiz, bg="orange")
quiz_submit_button.pack(pady=10)

# Footer
footer = tk.Label(root, text="Stay Vigilant. Protect Yourself from Phishing!", font=("Arial", 10, "italic"))
footer.pack(side="bottom", pady=10)

# Run the application
root.mainloop()
