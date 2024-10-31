import sqlite3
import tkinter as tk
from tkinter import messagebox

# Database setup
def setup_database():
    conn = sqlite3.connect('customer_feedback.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            feedback TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Submit feedback to the database
def submit_feedback():
    name = entry_name.get()
    email = entry_email.get()
    feedback = entry_feedback.get("1.0", tk.END).strip()

    if not name or not email or not feedback:
        messagebox.showerror("Input Error", "Please fill all fields.")
        return

    conn = sqlite3.connect('customer_feedback.db')
    c = conn.cursor()
    c.execute('INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)', (name, email, feedback))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Feedback submitted successfully!")
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_feedback.delete("1.0", tk.END)

# Retrieve and print data with password protection
def retrieve_data():
    password = input("Enter the password: ")
    if password == "yourpassword":  # Change this to your desired password
        conn = sqlite3.connect('customer_feedback.db')
        c = conn.cursor()
        c.execute('SELECT * FROM feedback')
        data = c.fetchall()
        conn.close()

        if data:
            print("Customer Feedback:")
            for entry in data:
                print(f"ID: {entry[0]}, Name: {entry[1]}, Email: {entry[2]}, Feedback: {entry[3]}")
        else:
            print("No feedback entries found.")
    else:
        print("Access denied. Incorrect password.")

# Create the GUI
root = tk.Tk()
root.title("Customer Feedback")

label_name = tk.Label(root, text="Name:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_email = tk.Label(root, text="Email:")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

label_feedback = tk.Label(root, text="Feedback:")
label_feedback.pack()
entry_feedback = tk.Text(root, height=5, width=30)
entry_feedback.pack()

submit_button = tk.Button(root, text="Submit", command=submit_feedback)
submit_button.pack()

retrieve_button = tk.Button(root, text="Retrieve Data", command=retrieve_data)
retrieve_button.pack()

setup_database()
root.mainloop()
