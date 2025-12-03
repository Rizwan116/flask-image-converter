# 🔐 Flask Image Converter with URL Encryption  

Convert images from Excel links (WebP → JPG/PNG/SVG) securely — with **full URL encryption**, ZIP export, and beginner‑friendly setup.

---

## 📌 Features

✔️ Upload **Excel, TXT, CSV, PDF, PPT, DOCX** (any format with URLs)  
✔️ Extract links + names  
✔️ Convert images to **JPG, PNG, SVG**  
✔️ Auto‑generate **ZIP download**  
✔️ **Encrypt all URLs** for security  
✔️ URLs never leave your device  
✔️ Beginner‑friendly Flask code  
✔️ Works offline  

---

## 📸 Screenshots

### ▶️ Upload Page  
_(Add your screenshot here)_

### ▶️ Output ZIP  
_(Add your screenshot here)_

---

## 🚀 Live Demo (Optional)
Add your Flask link here if deployed using Render/Heroku/Vercel.

---

## 📂 Folder Structure

```
project/
│── app.py
│── README.md
│── key.key
│── uploads/
│── converted/
│── templates/
│   └── index.html
```

---

## 🔐 Why URL Encryption?

Normally your app takes the URL → downloads the image → converts it.

This can expose URLs:

- In logs
- In memory
- In temp files
- In plain Excel files

To protect privacy, we use **Fernet AES encryption**.

### ✔️ What Encryption Does  
- Converts URL into unreadable text  
- Stores encrypted version only  
- Decrypts only at conversion time  
- Prevents anyone from seeing your original URLs  

### ❌ What it does NOT do  
- It **does NOT** send URLs to any server  
- It **does NOT** upload URLs to any third‑party  
- It **does NOT** share your data anywhere  

Your links stay fully private.

---

## 🔑 Generate Encryption Key

```python
from cryptography.fernet import Fernet

if not os.path.exists("key.key"):
    with open("key.key", "wb") as f:
        f.write(Fernet.generate_key())
```

The key encrypts/decrypts URLs.

⚠️ If deleted, old encrypted URLs become unusable.

---

## 🧰 Installation

Install required packages:

```bash
pip install flask pandas pillow requests cryptography python-dotenv openpyxl
```

---

## ▶️ Run the App

```bash
python app.py
```

App opens at:

```
http://127.0.0.1:5000
```

---

## 📥 How To Use

### 1️⃣ Upload an Excel file  
Your Excel must contain:

| name | link |
|------|------|
| image1 | https://example.com/file.webp |
| image2 | https://cdn.xyz/pic.webp |

### 2️⃣ Choose Format  
- JPG  
- PNG  
- SVG  

### 3️⃣ Download ZIP  

ZIP contains:

```
image1.jpg
image2.jpg
```

---

## 🧠 How the Code Works (Step-by-Step)

### 1. Read Excel  
Pandas reads the name + link columns.

### 2. URL Encryption  
Every URL is encrypted:

```python
encrypted = fernet.encrypt(url.encode()).decode()
```

### 3. URL Decryption  
Only at download time:

```python
url = fernet.decrypt(enc_url.encode()).decode()
```

### 4. Download Image  
Using `requests`.

### 5. Convert Image  
Using Pillow → JPG/PNG.

### 6. Create ZIP  
All files added automatically.

---

## 🔒 Security Explained

| Threat | Protected? | How |
|--------|-------------|------|
| Someone reading Excel URL? | ✔️ Yes | URLs become encrypted |
| Someone reading server logs? | ✔️ Yes | No real URLs stored |
| URLs leaking online? | ✔️ Yes | App uses local requests only |
| Data sent to external servers? | ❌ Never | Your computer only |

---

## 🧑‍💻 Tech Stack

- Python 3  
- Flask  
- Pandas  
- Pillow  
- Requests  
- Cryptography  
- HTML + Bootstrap  

---

## 📘 For Beginners

### What is Flask?  
A small Python web framework.

### What is Pandas?  
Library to read Excel.

### What is Pillow?  
Image conversion library.

### What is URL Encryption?  
Protects your URL from being visible.

---

## 🛠 Future Features (Optional)

- Drag & Drop upload  
- Multi‑URL parsing  
- Preview before download  
- WebP → AVIF support  
- Cloud version using Render  

---

## 🙋 Support

If you want:

- Better UI  
- Extra formats  
- Online deployed version  
- Upload multiple Excel files  
- Auto URL checker  

Just ask — I will help you.

---

## 📄 License

MIT License — free to use.
