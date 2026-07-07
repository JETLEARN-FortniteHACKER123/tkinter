import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv

class StudentMarksLogger:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Marks Logger")
        self.root.geometry("700x550")
        self.root.resizable(False, False)
        
        self.students = []
        self.current_student_index = None
        self.file_path = None
        
        self.create_widgets()
    
    def create_widgets(self):
        # Main Frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Student Marks Logger", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Name
        ttk.Label(main_frame, text="Name:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.name_entry = ttk.Entry(main_frame, width=30)
        self.name_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Roll Number
        ttk.Label(main_frame, text="Roll Number:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.roll_entry = ttk.Entry(main_frame, width=30)
        self.roll_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Science Marks
        ttk.Label(main_frame, text="Science Marks:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.science_entry = ttk.Entry(main_frame, width=30)
        self.science_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Maths Marks
        ttk.Label(main_frame, text="Maths Marks:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.maths_entry = ttk.Entry(main_frame, width=30)
        self.maths_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Percentage
        ttk.Label(main_frame, text="Percentage:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.percentage_entry = ttk.Entry(main_frame, width=30, state="readonly")
        self.percentage_entry.grid(row=5, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Buttons Frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=6, column=0, columnspan=2, pady=20)
        
        # Buttons
        ttk.Button(button_frame, text="Open", command=self.open_file).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Add/Update", command=self.add_update_student).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Edit", command=self.edit_student).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Delete", command=self.delete_student).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Save", command=self.save_file).pack(side=tk.LEFT, padx=5)
        
        # Students Listbox
        ttk.Label(main_frame, text="Students:").grid(row=7, column=0, columnspan=2, sticky=tk.W, pady=(10, 5))
        
        listbox_frame = ttk.Frame(main_frame)
        listbox_frame.grid(row=8, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        scrollbar = ttk.Scrollbar(listbox_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox = tk.Listbox(listbox_frame, yscrollcommand=scrollbar.set, height=8)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)
        scrollbar.config(command=self.listbox.yview)
    
    def calculate_percentage(self):
        try:
            science = float(self.science_entry.get())
            maths = float(self.maths_entry.get())
            percentage = (science + maths) / 2
            self.percentage_entry.config(state=tk.NORMAL)
            self.percentage_entry.delete(0, tk.END)
            self.percentage_entry.insert(0, f"{percentage:.2f}")
            self.percentage_entry.config(state="readonly")
        except ValueError:
            pass
    
    def add_update_student(self):
        name = self.name_entry.get().strip()
        roll = self.roll_entry.get().strip()
        
        if not name or not roll:
            messagebox.showerror("Error", "Name and Roll Number are required!")
            return
        
        try:
            science = float(self.science_entry.get())
            maths = float(self.maths_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Science and Maths marks must be numbers!")
            return
        
        self.calculate_percentage()
        percentage = self.percentage_entry.get()
        
        student = {
            "name": name,
            "roll": roll,
            "science": science,
            "maths": maths,
            "percentage": percentage
        }
        
        if self.current_student_index is not None:
            self.students[self.current_student_index] = student
            messagebox.showinfo("Success", "Student updated successfully!")
        else:
            self.students.append(student)
            messagebox.showinfo("Success", "Student added successfully!")
        
        self.refresh_listbox()
        self.clear_fields()
    
    def edit_student(self):
        if self.current_student_index is None:
            messagebox.showerror("Error", "Please select a student to edit!")
            return
        messagebox.showinfo("Info", "Edit the student details and click Add/Update")
    
    def delete_student(self):
        if self.current_student_index is None:
            messagebox.showerror("Error", "Please select a student to delete!")
            return
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this student?"):
            self.students.pop(self.current_student_index)
            self.refresh_listbox()
            self.clear_fields()
            messagebox.showinfo("Success", "Student deleted successfully!")
    
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if file_path:
            self.file_path = file_path
            try:
                self.students = []
                with open(file_path, 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        self.students.append(row)
                self.refresh_listbox()
                messagebox.showinfo("Success", "File opened successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {e}")
    
    def save_file(self):
        if not self.file_path:
            self.file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        
        if self.file_path:
            try:
                with open(self.file_path, 'w', newline='') as file:
                    fieldnames = ["name", "roll", "science", "maths", "percentage"]
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(self.students)
                messagebox.showinfo("Success", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")
    
    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for student in self.students:
            self.listbox.insert(tk.END, f"{student['name']} (Roll: {student['roll']})")
    
    def on_select(self, event):
        selection = self.listbox.curselection()
        if selection:
            self.current_student_index = selection[0]
            student = self.students[self.current_student_index]
            
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, student['name'])
            
            self.roll_entry.delete(0, tk.END)
            self.roll_entry.insert(0, student['roll'])
            
            self.science_entry.delete(0, tk.END)
            self.science_entry.insert(0, student['science'])
            
            self.maths_entry.delete(0, tk.END)
            self.maths_entry.insert(0, student['maths'])
            
            self.percentage_entry.config(state=tk.NORMAL)
            self.percentage_entry.delete(0, tk.END)
            self.percentage_entry.insert(0, student['percentage'])
            self.percentage_entry.config(state="readonly")
    
    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.roll_entry.delete(0, tk.END)
        self.science_entry.delete(0, tk.END)
        self.maths_entry.delete(0, tk.END)
        self.percentage_entry.config(state=tk.NORMAL)
        self.percentage_entry.delete(0, tk.END)
        self.percentage_entry.config(state="readonly")
        self.current_student_index = None
        self.listbox.selection_clear(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentMarksLogger(root)
    root.mainloop()
