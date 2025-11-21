# 🐍 Python Projects

> A collection of beginner-friendly Python applications built to practice and demonstrate fundamental programming concepts.

![Python](https://img.shields.io/badge/Python-3.x+-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

**Author:** [@Yoge-2004](https://github.com/Yoge-2004)

---

## 📑 Table of Contents

- [✨ About](#-about)
- [📦 Projects](#-projects)
- [⚙️ Requirements](#️-requirements)
- [🚀 Getting Started](#-getting-started)
- [💻 How to Run](#-how-to-run)
- [🎯 Features](#-features)
- [🤝 Contributing](#-contributing)
- [💬 Feedback](#-feedback)
- [📄 License](#-license)

---

## ✨ About

This repository showcases practical Python applications that cover essential programming concepts including:
- 🔄 Loops and Conditionals
- 📊 Data Structures (Dictionaries, Lists)
- 📥 User Input/Output Operations
- 🔧 Function Definitions and Modularization

Each project is a standalone script designed for learning purposes and demonstrates how to build interactive CLI applications.

---

## 📦 Projects

### 1. 🧮 Calculator Application

**Description:** A simple yet functional calculator that performs basic arithmetic operations.

**📋 Features:**
- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- 🏠 Floor Division
- ⚡ Exponentiation
- 📊 Modulus Operation
- 🆘 Built-in Help System
- ⭐ User Rating System

**📂 File:** `Calculator Application.py`

**🚀 Steps to Run:**

```bash
# Step 1: Open terminal/command prompt
# Step 2: Navigate to the project directory
cd Python-projects

# Step 3: Run the application
python "Calculator Application.py"
```

**📖 Usage Instructions:**

1. Read the help menu that displays available operators
2. Enter the first number when prompted
3. Enter the second number
4. Enter the desired operator (+, -, *, /, //, %, **)
5. View the calculated result
6. Choose to perform another calculation or exit

**🎯 Expected Outcome:**

```
Welcome to calculator application
Loading...
Press 
+ for Addition
- for Subtraction
* for Multiplication
/ for Division
// for floor division (integer division)
** for Exponentiation

Enter a number: 10
Enter another number: 5
Enter the operator: +
15
Do you want to perform any other calculation?
Enter (Yes/No): yes
```

---

### 2. 📇 Contact Book Application

**Description:** A digital contact management system that stores and manages your contacts in memory.

**📋 Features:**
- ➕ Add New Contacts
- 👁️ View All Contacts
- 🔍 Search Contacts
- ✏️ Update Contact Information
- 🗑️ Delete Contacts
- 📋 Display in Table Format
- ⭐ User Rating System

**📂 File:** `Contact Book Application.py`

**🚀 Steps to Run:**

```bash
# Step 1: Open terminal/command prompt
# Step 2: Navigate to the project directory
cd Python-projects

# Step 3: Run the application
python "Contact Book Application.py"
```

**📖 Usage Instructions:**

1. View the main menu with 5 options
2. **Add Contact (Option 1):** Enter name, address, email, and phone number
3. **View Contacts (Option 2):** Display all stored contacts in table format
4. **Search Contact (Option 3):** Enter a name to find contact details
5. **Update Contact (Option 4):** Modify existing contact information
6. **Delete Contact (Option 5):** Remove a contact from the book
7. Choose to continue or exit the application

**🎯 Expected Outcome:**

```
Welcome to our application
Loading...

Select:
1. Add a new contact
2. View contact list
3. Search a contact
4. Update a contact
5. Delete a contact
Enter your choice: 1

Enter name: John Doe
Enter address: 123 Main Street
Enter email address: john@example.com
Enter phone number: 555-1234

Do you want to perform any other operation?
Enter (Yes/No): yes
```

---

### 3. 🔐 Password Generator Application

**Description:** An automated password generation tool that creates secure random passwords.

**📋 Features:**
- 🎲 Random Password Generation
- 📏 Custom Length Configuration
- 🔤 Uppercase Letters (A-Z)
- 🔡 Lowercase Letters (a-z)
- 🔢 Numbers (0-9)
- 💡 Length Recommendations
- ⭐ User Rating System

**📂 File:** `Password Generator Application.py`

**🚀 Steps to Run:**

```bash
# Step 1: Open terminal/command prompt
# Step 2: Navigate to the project directory
cd Python-projects

# Step 3: Run the application
python "Password Generator Application.py"
```

**📖 Usage Instructions:**

1. Application starts and loads
2. Enter desired password length (recommended: 8 or more characters)
3. Receive a randomly generated password with mixed character types
4. Choose to generate another password or exit
5. Provide feedback rating on exit

**🎯 Expected Outcome:**

```
Welcome to Password Generator Application
Loading...

Enter the length of password (Recommended length:8): 12
Generated password is:  aB3xY9mK2pQr

Do you want to continue?
Enter (Yes/No): yes

Enter the length of password (Recommended length:8): 10
Generated password is:  Kj7Lm4Np9R

Do you want to continue?
Enter (Yes/No): no

Thanks for using my application.
```

---

### 4. 🎮 Rock Paper Scissors Game Application

**Description:** A classic interactive game where you compete against the computer AI.

**📋 Features:**
- 🤖 Computer AI Opponent
- 🏆 Score Tracking System
- 🎯 Win/Lose/Draw Logic
- 🔄 Multiple Rounds Support
- ⭐ User Rating System

**📂 File:** `Rock Paper Scissors Game Application.py`

**🚀 Steps to Run:**

```bash
# Step 1: Open terminal/command prompt
# Step 2: Navigate to the project directory
cd Python-projects

# Step 3: Run the application
python "Rock Paper Scissors Game Application.py"
```

**📖 Usage Instructions:**

1. Application loads and displays game rules
2. Choose your move:
   - Enter `1` for Rock
   - Enter `2` for Paper
   - Enter `3` for Scissors
3. View computer's choice
4. See game result (Win/Lose/Draw)
5. Check your current score
6. Play again or exit
7. Provide feedback rating

**🎯 Expected Outcome:**

```
Welcome to Rock Paper Scissors Game
Loading...

Enter:
1 for Rock
2 for Paper
3 for Scissors
Enter your choice: 2

Computer choice:  Rock
Your choice:  Paper
Won the game.

Do you want to play the game again?
Enter (Yes/No): yes

Enter:
1 for Rock
2 for Paper
3 for Scissors
Enter your choice: 1

Computer choice:  Scissors
Your choice:  Rock
Won the game.

Do you want to play the game again?
Enter (Yes/No): no

Thanks for using our application.
```

---

### 5. ✅ To-Do List Application

**Description:** A CLI-based task management system for organizing daily tasks by date.

**📋 Features:**
- 📅 Date-Based Task Organization (DD/MM/YYYY)
- ➕ Add Multiple Tasks
- ✏️ Update Existing Tasks
- 🗑️ Delete Task Lists
- 📊 Track Task Completion Status
- 📋 View All Tasks
- ⭐ User Rating System

**📂 File:** `To-Do list application using CLI.py`

**🚀 Steps to Run:**

```bash
# Step 1: Open terminal/command prompt
# Step 2: Navigate to the project directory
cd Python-projects

# Step 3: Run the application
python "To-Do list application using CLI.py"
```

**📖 Usage Instructions:**

1. Application loads and prompts for a date (DD/MM/YYYY format)
2. **If date doesn't exist:**
   - Choose to create a new to-do list
   - Enter tasks separated by commas and spaces
   - Tasks are automatically marked as "Not finished"
3. **If date already exists:**
   - View existing tasks and their status
   - Choose to:
     - **Option 1:** Update a task
     - **Option 2:** Delete the entire list
     - **Option 3:** Track task status
     - **Option 4:** Update task completion status
     - **Option 5:** View all tasks
4. Continue or exit the application
5. Provide feedback rating

**🎯 Expected Outcome:**

```
Welcome to To-do application
Loading...

Enter the date in the format(DD/MM/YYYY) format: 21/11/2025
Want to create a to-do list?
Enter 1 for Yes 2 for No: 1

Enter the items seperated by a comma and a space: Buy groceries, Complete project, Call mom

Do you want to continue?
Enter Yes or yes to Continue else Enter No or no: yes

Enter the date in the format(DD/MM/YYYY) format: 21/11/2025
To do list is already created.

21/11/2025 :
Tasks:  ['Buy groceries', 'Complete project', 'Call mom']
Status:  ['Not finished', 'Not finished', 'Not finished']

Do you wish to update or delete your to-do list?
Enter the number 1 to Update or 2 to Delete or 3 to Track or 4 to Update status of task or 5 to Print the to-do list: 4

Enter the item's number to be updated: 1
(Task 1 marked as Finished)

Do you want to continue?
Enter Yes or yes to Continue else Enter No or no: no

Thanks for using our application.
```

---

## ⚙️ Requirements

| Requirement | Details |
|-------------|---------|
| 🐍 Python | 3.x or higher |
| 🖥️ OS | Windows, macOS, or Linux |
| 📦 Dependencies | None (Standard Library only) |
| 💾 Disk Space | ~50 KB per application |

---

## 🚀 Getting Started

### Step 1️⃣ - Clone the Repository

```bash
git clone https://github.com/Yoge-2004/Python-projects.git
cd Python-projects
```

### Step 2️⃣ - Verify Python Installation

```bash
python --version
```

Ensure you have Python 3.x or higher installed.

### Step 3️⃣ - List Available Projects

```bash
ls
# or on Windows:
dir
```

---

## 💻 How to Run

### Quick Start

```bash
python "Application Name.py"
```

### Examples

```bash
# Run Calculator
python "Calculator Application.py"

# Run Contact Book
python "Contact Book Application.py"

# Run Password Generator
python "Password Generator Application.py"

# Run Rock Paper Scissors
python "Rock Paper Scissors Game Application.py"

# Run To-Do List
python "To-Do list application using CLI.py"
```

---

## 🎯 Features

✅ **Interactive CLI:** User-friendly command-line interfaces with clear prompts

✅ **Input Validation:** Handles user inputs with appropriate error checking

✅ **User Feedback:** Each application includes a 1-5 star rating system

✅ **Continuous Operation:** Applications loop until user chooses to exit

✅ **Learning-Friendly:** Well-commented code for easy understanding

✅ **No Dependencies:** Uses only Python standard library

✅ **Standalone Scripts:** Each project works independently

---

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

### Step 1️⃣ - Fork the Repository
Click the "Fork" button on GitHub

### Step 2️⃣ - Create a Feature Branch
```bash
git checkout -b feature/your-improvement
```

### Step 3️⃣ - Make Your Changes
Edit files and improve the projects

### Step 4️⃣ - Commit Your Changes
```bash
git commit -m "Add: Brief description of changes"
```

### Step 5️⃣ - Push to Your Branch
```bash
git push origin feature/your-improvement
```

### Step 6️⃣ - Open a Pull Request
Create a PR on GitHub with a clear description

### 💡 Contribution Ideas:

- 🐛 Add comprehensive error handling
- 💾 Implement file-based data persistence
- 📈 Enhance calculator with more operations
- 🎨 Create GUI versions using tkinter
- ⚡ Optimize code performance
- 🧪 Add unit tests
- 📚 Improve documentation
- 🌍 Add multi-language support

---

## 💬 Feedback

Each application includes a built-in feedback system. After using any application, you'll be prompted:

```
Do you want to give rating?
Enter (Yes/No): yes

Give the rating on the scale of 1(poor) to 5(best)
Enter the rating: 5
```

Your feedback helps improve these applications! 🌟

---

## 📄 License

This project is open source and available under the **MIT License**.

You are free to:
- ✅ Use these projects for personal and commercial purposes
- ✅ Modify and redistribute the code
- ✅ Include the projects in your own applications

See the [LICENSE](LICENSE) file for full details.

---

## 📞 Support

Found a bug? Have a suggestion? Here's how to reach out:

- 🐛 **Report Issues:** [Open an Issue](https://github.com/Yoge-2004/Python-projects/issues)
- 💬 **Discussions:** [Start a Discussion](https://github.com/Yoge-2004/Python-projects/discussions)
- 📧 **Contact:** [@Yoge-2004](https://github.com/Yoge-2004)

---

## 🎉 Enjoy Exploring Python with These Practical Applications!

```
╔═══════════════════════════════════════════════╗
║   Happy Coding! 🚀                            ║
║   Made with ❤️ by Yoge-2004                  ║
║   Last Updated: 2025-11-21 08:31:28 UTC     ║
╚═══════════════════════════════════════════════╝
```

---

**⭐ If you found this helpful, please star the repository!**