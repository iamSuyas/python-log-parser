# Log Parser Web Application

## Description

This is a simple Flask-based web application that allows users to upload `.txt` log files and scans them for suspicious activity. The system checks for specific patterns such as "failed login", "unauthorized access", or "malicious activity detected" and returns a list of alerts with the corresponding timestamps (if available).

---

## How to Run the Project

### 1. Clone the repository:
```bash
git clone https://github.com/iamSuyas/python-log-parser
cd python-log-parser
```

### 2. Create and activate a virtual environment:
```bash
python -m venv venv
venv/bin/activate
```

### 3. Install required dependencies:
```bash
pip install -r requirements.txt
```
### 4. Setup Secret key for CSRF token
- Add a variable `SECRET_KEY` in a `.env` file like:
```bash
SECRET_KEY=secret_key_example
```

### 5. Run the Flask application:
```bash
python app.py
```


### 5. Assumptions & Limitations
- The parser only supports .txt files encoded in UTF-8.

- The timestamp extraction assumes formats like:
    - Aug 01 12:34:56
    - 2025-08-01 12:34:56

- The list of suspicious patterns is hardcoded and may not cover all possible attack signatures.

- The file content is read and parsed in-memory; this is not suitable for very large files.

- The system does not store any data. All parsing is done in-session and is temporary.

- No authentication is added. So it is not suitable for production environment  

- You can use the `system_logs.txt` file for parsing data. Note that it is only a `representation` of a system log and not a real-world application's system log




