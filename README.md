# Email-Client-Application

### This script provides a basic email sending and receiving application using Python's tkinter library for GUI and the smtplib and imaplib libraries for sending and fetching emails, respectively.

## Email Sending Application:
### This part allows users to compose an email with a sender's email, password, recipient's email, subject, and body.
### It uses smtplib to send emails through an SMTP server (in this case, Outlook's SMTP server).
### The send_email function takes sender's email, password, recipient's email, subject, and body as arguments, constructs an email message using MIMEMultipart and MIMEText, and sends the email through the SMTP server.
### The send function gets the input values from the GUI fields, calls the send_email function, and displays a message box indicating whether the email was sent successfully or not.

## Email Receiving Application:
### This part allows users to fetch the latest email from their inbox using IMAP protocol.
### It uses imaplib to connect to the IMAP server (in this case, Outlook's IMAP server) and fetch the latest email from the inbox.
### The fetch_latest_email function takes the user's email and password as input, connects to the IMAP server, searches for the latest email, fetches its content, and displays the email body in a message box.

### In both applications, tkinter is used to create the GUI, including entry fields for email addresses and passwords, buttons to trigger sending or receiving emails, and message boxes to display email content or error messages.
