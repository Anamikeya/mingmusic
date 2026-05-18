# 🚀 Django Starter Project

A clean, production-ready Django and react boilerplate configuration. This repository is released under the **WTFPL (Do What the Fuck You Want To Public License)**. You are free to modify, distribute, and use this code however you see fit.

---

## ⚠️ Important: Before You Start

You must complete the **Project Renaming** steps below **BEFORE** creating your virtual environment or installing `requirements.txt`. Failing to do so will cause `ModuleNotFoundError` errors.

---

## 🛠️ Project Customization (Renaming)

Follow these steps to rename `mingmusic` to your custom project name:

### 1. Rename the Core Directory
Rename the inner configuration folder containing `settings.py` from `mingmusic` to your desired project name (e.g., `my_project`).
```text
your-repository/
│   manage.py
└───mingmusic/   ──>   Rename this folder to: my_project/
```

### 2. Update Configuration Files
Open the following files in your code editor and replace every occurrence of the text `mingmusic` with your new project name:
* `manage.py`
* `[your_new_name]/settings.py`
* `[your_new_name]/urls.py`
* `[your_new_name]/wsgi.py`
* `[your_new_name]/asgi.py`

---

## ⚙️ Installation & Setup

Once the project is successfully renamed, execute the following commands in your terminal:

### 1. Create a Virtual Environment
```bash
python -m venv venv
```

### 2. Activate the Environment
* **Windows (Command Prompt):**
  ```cmd
  venv\Scripts\activate
  ```
* **Windows (PowerShell):**
  ```powershell
  venv\Scripts\Activate.ps1
  ```
* **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Upgrade Pip & Install Dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py migrate
```

### 5. Start the Development Server
```bash
python manage.py runserver
```
Navigate to `http://127.0.0.1` in your browser to view the running application.

---

## 📜 License

This project is licensed under the **WTFPL** – Do What the Fuck You Want To Public License. See the [WTFPL Website](http://wtfpl.net) for more details.
