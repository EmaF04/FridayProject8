# FridayProject8
Customer Feedback Management System
This Python application provides a graphical interface for users to submit and manage customer feedback, storing entries in a local SQLite database. It uses tkinter for the graphical interface and sqlite3 to handle database operations.

Features
Add Feedback: Users can submit their name, email, and feedback.
Retrieve Feedback: Allows retrieval of all feedback entries (password-protected).
Database: Feedback entries are stored in a local SQLite database named customer_feedback.db.

Usage

Launching the Application:
Run the application script to launch the feedback management window.

Adding Feedback:
Enter your name, email, and feedback in the respective fields, and click the Submit button.
If all fields are filled out correctly, a success message will appear.
If any fields are left blank, a warning will prompt you to fill in all information.

Retrieving Feedback:
Click the Retrieve Feedback button.
Enter the password to access stored feedback (default is "your_password"; replace this in the code as needed).
Feedback entries will be displayed in the console, listing ID, name, email, and feedback details.

Code Overview

Database Setup: The create_database function initializes the database and creates a feedback table if it doesn’t exist.

Submit Feedback: The submit_feedback function inserts feedback into the database.

Retrieve Feedback: The retrieve_feedback function displays all feedback entries upon entering the correct password.

GUI (FeedbackApp Class): The FeedbackApp class creates a user interface for the application using tkinter. It includes:
submit: Handles feedback submission and shows messages using messagebox.
retrieve: Requests a password to display all feedback entries.
clear_entries: Clears input fields after submission.

Customization
Password: Modify the retrieve_feedback function to change the password used for data retrieval. The current password is p@$$w0rd.