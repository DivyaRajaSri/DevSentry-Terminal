# 🔰 DevSentry – Code Scanner for Secrets

DevSentry is a terminal-based Python tool that scans source code folders to find **hardcoded secrets** like:
- Passwords
- API keys (AWS, Google, etc.)
- Email IDs
- Indian phone numbers

---

## 🔧 Features

✅ Scans all files inside a folder  
✅ Detects patterns using Regex  
✅ Shows pattern, file name, and line number  
✅ Saves the results as JSON report  
✅ Works fully in the terminal  
✅ Built using beginner-friendly Python!

---

## 📸 Example Output


![Scan Result](output.png)


📄 File: test_files/sample_code.py
🔎 Pattern: AWS Key
📌 Line 3: aws_key = "AKIAIOSFODNN7EXAMPLE"

✅ Report saved to: reports/scan_report_2025_07_16_103120.json


---

## 🛠 Technologies Used

- Python 🐍
- Regex (Pattern Matching)
- Terminal Input/Output
- JSON
- (Optional in future: Flutter for mobile/web)

---

## 🧠 Why This Project?

Built as a security tool to help developers **check their code for sensitive information** before pushing to GitHub or deploying.

---

## 👩‍💻 Author

👋 **Divya Raja Sri Malluvalasa**  
B.Tech, 3rd Year – Cybersecurity & IoT  
