# SmartFileIntegrityModel
Smart File Integrity Monitoring System using Python (CodTech Internship Task 1)

## 📌 Description

The **Smart File Integrity Monitoring System** is a cybersecurity-based project developed as part of my **CodTech Internship (Task 1)** in the domain of **Cybersecurity and Ethical Hacking**.

This system is designed to monitor a specified folder in real time and detect any unauthorized or suspicious changes to files. It uses **SHA256 cryptographic hashing** to verify file integrity and ensures that even the smallest modification in a file is identified.

The system continuously tracks file activities such as **creation, modification, and deletion**, and generates alerts when changes are detected. All events are recorded in a log file for further analysis.

Additionally, the project includes an interactive **dashboard built using Streamlit**, which visually displays system activity, logs, and monitoring status—similar to basic tools used in **Security Operations Centers (SOC)**.

A launcher script (`start_system.py`) is also provided to run both the monitoring system and dashboard simultaneously, making the tool more user-friendly and efficient.

This project demonstrates practical implementation of key cybersecurity concepts such as:

* File Integrity Monitoring (FIM)
* Cryptographic hashing (SHA256)
* Real-time system monitoring
* Intrusion detection techniques
* Security logging and analysis

Overall, this project provides a foundational understanding of how real-world cybersecurity systems detect file tampering and unauthorized system changes.

