import tkinter as tk
from tkinter import messagebox
import json
import os

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to remove a selected task
def remove_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
        save_tasks()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

# Function to mark a task as complete
def complete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        task = f"{task} - Completed"
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(tk.END, task)
        save_tasks()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to mark complete.")

# Function to load tasks from a JSON file
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                tasks_listbox.insert(tk.END, task)

# Function to save tasks to a JSON file
def save_tasks():
    tasks = tasks_listbox.get(0, tasks_listbox.size())
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Main application window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")

# Task entry box
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Add task button
add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

# Tasks listbox
tasks_listbox = tk.Listbox(root, height=10, width=40)
tasks_listbox.pack(pady=10)

# Complete and remove task buttons
complete_task_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_task_button.pack(pady=5)

remove_task_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_task_button.pack(pady=5)

# Load tasks when the program starts
load_tasks()

# Start the application
root.mainloop()
