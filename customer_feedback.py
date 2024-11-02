import sqlite3
import tkinter as tk
from tkinter import messagebox

# Set up the database
conn = sqlite3.connect('feedback.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS feedback
             (name TEXT, email TEXT, feedback TEXT)''')
conn.commit()
# Function to submit feedback
def submit_feedback():
    name = entry_name.get()
    email = entry_email.get()
    feedback = entry_feedback.get()

    if name and email and feedback:
        c.execute("INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)", (name, email, feedback))
        conn.commit()
        messagebox.showinfo("Success", "Feedback submitted successfully!")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_feedback.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

# Function to retrieve and print feedback (with password protection)
def retrieve_feedback():
    password = input("Enter password to access feedback data: ")
    if password == "codingisawesome":
        c.execute("SELECT * FROM feedback")
        feedback_data = c.fetchall()
        if feedback_data:
            print("\n--- All Feedback Entries ---")
            for entry in feedback_data:
                print(f"Name: {entry[0]}, Email: {entry[1]}, Feedback: {entry[2]}")
        else:
            print("No feedback entries found.")
    else:
        print("Access Denied: Incorrect password.")

# GUI setup
root = tk.Tk()
root.title("Customer Feedback Application")

# Name input
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

# Email input
label_email = tk.Label(root, text="Email:")
label_email.grid(row=1, column=0, padx=10, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=10)

# Feedback input
label_feedback = tk.Label(root, text="Feedback:")
label_feedback.grid(row=2, column=0, padx=10, pady=10)
entry_feedback = tk.Entry(root)
entry_feedback.grid(row=2, column=1, padx=10, pady=10)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_feedback)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Retrieve data button
retrieve_button = tk.Button(root, text="Retrieve Data", command=retrieve_feedback)
retrieve_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()

# Close the database connection when the app is closed
conn.close()
