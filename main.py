from cProfile import label
import tkinter as tk
from tkinter import PhotoImage
import sqlite3
import time

def button_click():
    contents_window = tk.Toplevel(root)
    contents_window.title("About")

    with open("readMore.txt", "r") as file:
        contents = file.read()
    
    title_label = tk.Label(contents_window, text="About", font=("TkDefaultFont", 14))
    title_label.pack()

    label = tk.Text(contents_window, height=20, width=50)
    label.insert("1.0", contents)
    label.pack()

def button_click0():
    new_window = tk.Toplevel(root)
    new_window.title("Save to Database")

    message_label = tk.Label(new_window, text="Enter message:")
    message_label.pack()

    message_entry = tk.Entry(new_window)
    message_entry.pack()
    
    name_label = tk.Label(new_window, text="Enter Name:")
    name_label.pack()

    name_entry = tk.Entry(new_window)
    name_entry.pack()

    submit_button = tk.Button(new_window, text="Submit", command=lambda: save_to_database(message_entry.get(), name_entry.get()))
    submit_button.pack()

def save_to_database(message, name):
    # Code to save the message to the database using SQL
    print("Saving message to database:", message, name)
    conn = sqlite3.connect("mydatabase.db")
    c = conn.cursor()
    
    current_timestamp = time.time()
    print(current_timestamp)

    c.execute("CREATE TABLE IF NOT EXISTS data (col1 text, col2 text, col3 text)")
    c.execute("INSERT INTO data VALUES (?,?,?)", (message, name, current_timestamp))

    conn.commit()
    conn.close()


def button_click11():
    new_window = tk.Toplevel(root)
    new_window.title("New Window Three")
    label = tk.Label(new_window, text="This is a third window.")
    label.pack()

    import sqlite3

def button_click1():
    display_window = tk.Toplevel(root)
    display_window.title("Display Data")

    title_label = tk.Label(display_window, text="Data from the database", font=("TkDefaultFont", 14))
    title_label.pack()

    display_text = tk.Text(display_window, height=20, width=60)
    display_text.pack()

    conn = sqlite3.connect("mydatabase.db")
    c = conn.cursor()

    c.execute("SELECT * FROM data")
    data = c.fetchall()

    for row in data:
        display_text.insert(tk.END, str(row))
        display_text.insert(tk.END, '\n')

    conn.close()



root = tk.Tk()
root.title("Simple Tkinter App")

globe_icon = PhotoImage(file="globe.png")
root.iconphoto(False, globe_icon)

P1 = "This is a Python file which will save to a databse and pull from a database and display it using a tkinter GUI. "
P2 = "Want to save things in the databse well this file can"
P3 = "Want to look at things in the database well you can in this file"

B1 = "Read More"
B2 = "Save to DataBase"
B3 = "Read from DataBase"

title = tk.Label(root, text="Welcome to my Tkinter app!", font=("Helvetica", 16))
title.grid(row=0, column=0, columnspan=2, pady=10)

paragraph1 = tk.Label(root, text=P1)
paragraph1.grid(row=1, column=0, pady=10)
button = tk.Button(root, text=B1, command=button_click)
button.grid(row=1, column=1, columnspan=2, pady=10)

paragraph2 = tk.Label(root, text=P2)
paragraph2.grid(row=3, column=0, pady=10)
button = tk.Button(root, text=B2, command=button_click0)
button.grid(row=3, column=1, columnspan=2, pady=10)

paragraph3 = tk.Label(root, text=P3)
paragraph3.grid(row=5, column=0, pady=10)
button = tk.Button(root, text=B3, command=button_click1)
button.grid(row=5, column=1, columnspan=2, pady=10)

root.mainloop()
