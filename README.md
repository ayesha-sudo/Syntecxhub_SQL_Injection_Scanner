📌 SQL Injection Scanner (Python)

This project is a Python-based SQL Injection Scanner designed to identify basic SQL injection vulnerabilities in web applications. The tool automates the process of sending crafted payloads to input parameters and analyzing server responses for common database error messages.

The scanner supports multi-threading for faster execution, includes rate limiting to avoid overwhelming the server, and logs all tested payloads along with detected vulnerabilities into a report file.

This project is intended for educational and ethical use only, specifically for testing authorized targets such as local applications and vulnerable environments like DVWA.

🚀 Features

Automated SQL injection payload testing

Detection of database error-based vulnerabilities

Multithreading for improved performance

Rate limiting to control request speed

Generates a detailed report file (TXT)

Simple and easy-to-use command-line interface

🛠️ Technologies Used

Python

Requests library

Threading

⚠️ Disclaimer

This tool is developed strictly for educational purposes. Do not use it on unauthorized websites or systems. Only test on:

DVWA (Damn Vulnerable Web App)

Localhost applications

Authorized testing environments
