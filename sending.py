import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach body to message
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server with longer timeout
        with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp_conn:
            smtp_conn.starttls()
            smtp_conn.login(sender_email, sender_password)
        
            # Send email
            smtp_conn.send_message(msg)
        
        return "Email sent successfully."
    except Exception as e:
        return f"An error occurred while sending the email: {e}"

def send():
    sender_email = sender_email_entry.get()
    sender_password = sender_password_entry.get()
    recipient_email = recipient_email_entry.get()
    subject = subject_entry.get()
    body = body_entry.get("1.0", "end-1c")  # Get the text from the body text widget

    message = send_email(sender_email, sender_password, recipient_email, subject, body)
    messagebox.showinfo("Success", f"{message}")

root = tk.Tk()
root.title("Email Sender")
root.geometry("400x300")

# Colors
bg_color = "#f0f0f0"
button_bg_color = "#4CAF50"
button_fg_color = "white"
entry_bg_color = "#e0e0e0"

# Create a custom style for buttons
def send_button_hover(e):
    send_button.config(bg="green")

def send_button_leave(e):
    send_button.config(bg=button_bg_color)

# Create widgets
sender_email_label = tk.Label(root, text="Sender's Email:", bg=bg_color)
sender_email_label.grid(row=0, column=0, sticky="e")
sender_email_entry = tk.Entry(root, bg=entry_bg_color)
sender_email_entry.grid(row=0, column=1)

sender_password_label = tk.Label(root, text="Password:", bg=bg_color)
sender_password_label.grid(row=1, column=0, sticky="e")
sender_password_entry = tk.Entry(root, show="*", bg=entry_bg_color)
sender_password_entry.grid(row=1, column=1)

recipient_email_label = tk.Label(root, text="Recipient's Email:", bg=bg_color)
recipient_email_label.grid(row=2, column=0, sticky="e")
recipient_email_entry = tk.Entry(root, bg=entry_bg_color)
recipient_email_entry.grid(row=2, column=1)

subject_label = tk.Label(root, text="Subject:", bg=bg_color)
subject_label.grid(row=3, column=0, sticky="e")
subject_entry = tk.Entry(root, bg=entry_bg_color)
subject_entry.grid(row=3, column=1)

body_label = tk.Label(root, text="Body:", bg=bg_color)
body_label.grid(row=4, column=0, sticky="ne")
body_entry = tk.Text(root, height=10, width=30, bg=entry_bg_color)
body_entry.grid(row=4, column=1)

send_button = tk.Button(root, text="Send Email", bg=button_bg_color, fg=button_fg_color, command=send)
send_button.grid(row=5, columnspan=2, pady=10)
send_button.bind("<Enter>", send_button_hover)
send_button.bind("<Leave>", send_button_leave)

root.mainloop()