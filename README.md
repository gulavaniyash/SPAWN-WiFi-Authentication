# SPAWN: A Lightweight and Secure Privacy-Preserving Wi-Fi Authentication Protocol

## 📌 Overview

SPAWN (Secure Privacy-preserving Authentication for Wi-Fi Networks) is a lightweight and secure authentication protocol designed to enhance user privacy and security in wireless networks. It addresses key limitations of traditional protocols like WPA2 and WPA3, such as identity exposure and high computational overhead.

---

## 🚀 Features

* 🔐 Privacy protection using Temporary IDs (Temp-ID)
* 🛡️ Secure authentication using HMAC
* 🔑 ECC-based key exchange (lightweight and secure)
* ⚡ Latency measurement and performance analysis
* 📊 Automatic graph generation (Matplotlib)

---

## 🧠 Key Concepts

* **Temp-ID:** Dynamically generated identifier to prevent device tracking
* **HMAC:** Ensures data integrity and authentication
* **ECC (Elliptic Curve Cryptography):** Secure and efficient key exchange
* **Nonce & Timestamp:** Prevent replay attacks

---

## 🛠️ Technologies Used

* Python
* Socket Programming
* Cryptography Library
* Matplotlib
* Wireshark (for packet analysis)

---

## 📂 Project Structure

```
wifi-auth-project/
│
├── main.py
├── graphs.py
├── latency.png
├── security.png
├── privacy.png
├── overhead.png
└── README.md
```

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install cryptography matplotlib
```

2. Run the project:

```bash
python main.py
```

---

## 📊 Output

* Temp-ID generation
* HMAC verification
* ECC-based shared key generation
* Latency measurement
* Performance graphs

---

## 🔍 Performance Analysis

The protocol is evaluated based on:

* Latency
* Security level
* Privacy protection
* Computational overhead

Graphs are automatically generated and saved as images.

---

## ⚠️ Note

This is a **prototype implementation** developed using Python.
In real-world deployment, the protocol would be integrated into Wi-Fi firmware or network stacks.

---

## 🔮 Future Work

* Real hardware implementation
* Integration with Wi-Fi firmware
* Advanced attack simulations (MITM, replay attacks)
* NS-3 based network simulation

---

## 👨‍💻 Author

**Yash Gulvani**
M.Tech Computer Science and Engineering

---

## 📜 License

This project is developed for academic and research purposes.

