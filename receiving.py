import imaplib
import email
import tkinter as tk
from tkinter import messagebox

def fetch_latest_email():
    username = username_entry.get()
    password = password_entry.get()
    
    try:
        # Connect to IMAP server
        with imaplib.IMAP4_SSL('imap-mail.outlook.com') as imap_conn:
            imap_conn.login(username, password)
            imap_conn.select('inbox')

            # Search for latest email
            typ, data = imap_conn.search(None, 'ALL')
            latest_email_id = data[0].split()[-1]

            # Fetch latest email
            typ, email_data = imap_conn.fetch(latest_email_id, '(RFC822)')
            raw_email = email_data[0][1]
            email_message = email.message_from_bytes(raw_email)

            # Extract email body
            if email_message.is_multipart():
                for part in email_message.walk():
                    if part.get_content_type() == 'text/plain':
                        email_body = part.get_payload(decode=True).decode('utf-8')
                        messagebox.showinfo("Email Message", email_body)
                        break
            else:
                email_body = email_message.get_payload(decode=True).decode('utf-8')
                messagebox.showinfo("Email Message", email_body)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while fetching the email: {e}")

# Create main window
root = tk.Tk()
root.title("Email Receiver")

# Create labels and entry fields for email and password
tk.Label(root, text="Email:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Button to fetch email
fetch_button = tk.Button(root, text="Receive", command=fetch_latest_email, bg="#4CAF50", fg="white")
fetch_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
