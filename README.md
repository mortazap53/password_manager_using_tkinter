# Tkinter Password Manager

A simple **Python GUI password manager** built with Tkinter. Generate strong passwords, store them locally, and copy them to your clipboard instantly.

---

## Features

- Generate **random strong passwords** with letters, numbers, and symbols.
- Save passwords with website and email/username to a local file (`passwords.txt`).
- Automatically copy generated passwords to clipboard.
- User-friendly GUI interface with Tkinter. Providing two one error popup and another one okchecker popups for user.
- Pre-fills your email/username for convenience.

---

## Usage:

- Enter the Website, Email/Username, and Password.
- Click Generate Password to automatically create a strong password.
- Click Add to save the entry to passwords.txt.
- The password will also be copied to your clipboard automatically.

## File sructure:
tk-password-manager/
==> main.py          # Main application
==> logo.png         # App logo
==> passwords.txt    # Stored passwords (auto-generated)
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

3. Testing
   
 Test UI layout and usability ==> [ ].
 Test password generation ==> [ ].
 Test saving to file ==> [ ].
 Test error handling for empty fields ==> [ ].
 Test clipboard functionality ==> [ ].

Tech Stack
* Python 3
* Tkinter (GUI)
* Pyperclip (clipboard support)
* Random (password generation)

### Author:
Mortaza Panahi.
mortazap53
