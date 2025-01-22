import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_application():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    job_role = job_role_entry.get()
    cover_letter = cover_letter_text.get("1.0", tk.END).strip()

    # Validation for empty fields
    if not name or not email or not phone or not job_role:
        messagebox.showerror("Error", "All fields are required!")
        return

    # Simulate submission (print details to console or save to a file/database)
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Job Role: {job_role}")
    print(f"Cover Letter: {cover_letter}")

    # Display success message
    messagebox.showinfo("Application Submitted", "Your application has been submitted successfully!")

    # Clear all fields after submission
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    job_role_entry.delete(0, tk.END)
    cover_letter_text.delete("1.0", tk.END)

# Create the main tkinter window
root = tk.Tk()
root.title("Job Application Form")
root.geometry("400x500")

# Title label
tk.Label(root, text="Job Application Form", font=("Arial", 16)).pack(pady=10)

# Name label and entry
tk.Label(root, text="Full Name:").pack(anchor="w", padx=20, pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack(padx=20)

# Email label and entry
tk.Label(root, text="Email:").pack(anchor="w", padx=20, pady=5)
email_entry = tk.Entry(root, width=40)
email_entry.pack(padx=20)

# Phone number label and entry
tk.Label(root, text="Phone Number:").pack(anchor="w", padx=20, pady=5)
phone_entry = tk.Entry(root, width=40)
phone_entry.pack(padx=20)

# Job Role label and entry
tk.Label(root, text="Job Role:").pack(anchor="w", padx=20, pady=5)
job_role_entry = tk.Entry(root, width=40)
job_role_entry.pack(padx=20)

# Cover Letter label and text box
tk.Label(root, text="Cover Letter:").pack(anchor="w", padx=20, pady=5)
cover_letter_text = tk.Text(root, width=40, height=5)
cover_letter_text.pack(padx=20, pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit Application", command=submit_application)
submit_button.pack(pady=20)

# Run the tkinter event loop
root.mainloop()
