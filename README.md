# 🔐 Flask Image Converter with URL Encryption  

Convert images from Excel links (WebP → JPG/PNG/SVG) securely — with **full URL encryption**, ZIP export, and beginner‑friendly setup.

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

## 🧑‍💻 Tech Stack

- Python 3  
- Flask  
- Pandas  
- Pillow  
- Requests  
- Cryptography  
- HTML + Bootstrap  

---

## 📄 License

MIT License — free to use.
