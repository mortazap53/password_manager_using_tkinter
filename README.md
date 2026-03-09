Good — this version is actually a real upgrade. You added two things that matter:

JSON storage instead of plain text

Search functionality

Those are meaningful features, so the README must reflect them. Your previous README is now outdated, especially in:

Features

Usage

File structure

Functionality description

Checklist

Below is a fully updated README, one copy-paste block for GitHub.

# Tkinter Password Manager

A simple **Python GUI Password Manager** built with Tkinter.  
It can **generate strong passwords, store them in a JSON file, and search for saved credentials**.

---

# Features

- Generate **strong random passwords** with letters, numbers, and symbols.
- Automatically **copy generated passwords to clipboard**.
- Save credentials (**website, email/username, password**) to a **JSON database**.
- **Search saved passwords by website**.
- Clean and simple **Tkinter GUI interface**.
- Error handling for:
  - Missing password file
  - Empty fields
  - Corrupted JSON file

---

## Usage:

- Enter the Website, Email/Username, and Password.
- Click Generate Password to automatically create a strong password.
- Click Add to save the entry to passwords.txt.
- The password will also be copied to your clipboard automatically.
- Searching for the password and email via the attached website.

## File sructure:
tk-password-manager/
==> main.py          # Main application
==> logo.png         # App logo
==> passwords.txt    # Stored passwords (auto-generated) (searching password)
==> README.md        # This file

## Development checklist:
a perfect todo checklist from the begining up to the end of building this project:
1. User Interface (UI)

 Create main window with Tkinter ==> [ ].
 Insert app logo ==> [ ].
 Add labels: Website, Email/Username, Password ==> [ ].
 Add entry fields: Website, Email/Username, Password ==> [ ].
 Add buttons: ==> [ ].
 "Add" → Save data to file
 "Generae Password" → Generate and insert strong password

2. Functionality
   
2.1 Saving Passwords
 Collect Website, Email, and Password inputs ==> [ ].
 Validate that no field is empty → show error if empty ==> [ ].
 Show user a confirmation overview before saving ==> [ ].
 Write entry to passwords.txt file ==> [ ].

2.2 Generating Passwords
 Generate strong password with letters, numbers, and symbols ==> [ ].
 Insert generated password into password entry field ==> [ ].
 Copy generated password to clipboard automatically ==> [ ].

2.3 Searching Passwords
 Load JSON data ==> [ ].
 Search website key ==> [ ].
 Show stored email and password ==> [ ].
 Show error if website not found ==> [ ].
 Handle missing JSON file ==> [ ].

3. Testing
   
 Test UI layout and usability ==> [ ].
 Test password generation ==> [ ].
 Test saving to file ==> [ ].
 Test error handling for empty fields ==> [ ].
 Test clipboard functionality ==> [ ].

Technologies Used:
* Python 3
* Tkinter (GUI)
* JSON
* Pyperclip (clipboard support)
* Random (password generation)

### Author:
Mortaza Panahi.
mortazap53
