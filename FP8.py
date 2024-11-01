import sqlite3
from tkinter import *
from tkinter import messagebox

# Database setup
def create_database():
    conn = sqlite3.connect('customer_feedback.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            feedback TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Insert feedback into the database
def submit_feedback(name, email, feedback):
    conn = sqlite3.connect('customer_feedback.db')
    c = conn.cursor()
    c.execute('INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)', (name, email, feedback))
    conn.commit()
    conn.close()

# Retrieve feedback from the database
def retrieve_feedback(password):
    if password == "p@$$w0rd":  # Replace with your password
        conn = sqlite3.connect('customer_feedback.db')
        c = conn.cursor()
        c.execute('SELECT * FROM feedback')
        entries = c.fetchall()
        conn.close()
        for entry in entries:
            print(f"ID: {entry[0]}, Name: {entry[1]}, Email: {entry[2]}, Feedback: {entry[3]}")
    else:
        print("Access Denied: Incorrect password.")

# GUI class
class FeedbackApp:
    def __init__(self, master):
        self.master = master
        master.title("Customer Feedback")

        self.name_label = Label(master, text="Name:")
        self.name_label.pack()
        self.name_entry = Entry(master)
        self.name_entry.pack()

        self.email_label = Label(master, text="Email:")
        self.email_label.pack()
        self.email_entry = Entry(master)
        self.email_entry.pack()

        self.feedback_label = Label(master, text="Feedback:")
        self.feedback_label.pack()
        self.feedback_entry = Text(master, height=5, width=30)
        self.feedback_entry.pack()

        self.submit_button = Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()

        self.retrieve_button = Button(master, text="Retrieve Feedback", command=self.retrieve)
        self.retrieve_button.pack()

    def submit(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        feedback = self.feedback_entry.get("1.0", END).strip()
        if name and email and feedback:
            submit_feedback(name, email, feedback)
            messagebox.showinfo("Success", "Feedback submitted successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def retrieve(self):
        password = input("Enter the password to retrieve data: ")
        retrieve_feedback(password)

    def clear_entries(self):
        self.name_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.feedback_entry.delete("1.0", END)


create_database()
root = Tk()
app = FeedbackApp(root)
root.mainloop()
