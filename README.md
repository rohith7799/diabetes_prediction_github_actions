# 🩺 Diabetes Prediction API (FastAPI)

This project is a **FastAPI-based API** for predicting diabetes based on user-provided medical details.  
The model used here is a pre-trained **machine learning model** stored in `trained_model/diabetes_model.pkl`.
In this project, I have implemented the Github actions which will trigger when any push or pull request is made.
---

## 📂 Project Structure

```
project-root/
│
├── main.py                              # FastAPI application
├── trained_model/
│   └── diabetes_model.pkl               # Pickle file containing trained ML model
├── requirements.txt                     # Python dependencies
└── README.md                            # Project documentation
```

---

## 🚀 Features
- Accepts JSON input with medical parameters such as pregnancies, glucose, insulin, etc.
- Uses a pre-trained ML model to predict diabetes.
- Returns prediction in a structured JSON format.

---

## 🛠 Installation & Setup

1️⃣ **Clone this repository**
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

2️⃣ **Create and activate a virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
```

3️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

4️⃣ **Run the FastAPI app**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at:  
🔗 **Docs UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
🔗 **Redoc UI** → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📤 API Endpoint

**POST** `/diabetes_prediction`  
**Example Request:**
```json
{
  "pregnancies": 2,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 20,
  "Insulin": 85,
  "BMI": 25.5,
  "DiabetesPedigreeFunction": 0.5,
  "Age": 30
}
```

**Example Response:**
```json
{
  "label": 0,
  "result": "The person is not diabetic"
}
```

---

## 📦 Git Commands to Upload This Project to GitHub

**Initialize Git & Commit Your Code**
```bash
git init
git add .
git commit -m "Initial commit - Diabetes Prediction API"
```

**Add Remote Repository**
```bash
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
```

**Push Code to GitHub**
```bash
git branch -M main
git push -u origin main
```
---

## ⚡ GitHub Actions (CI/CD)
You can create a `.github/workflows/ci.yml` file to automate testing and deployment.  
Example GitHub Actions workflow:
```yaml
name: FastAPI CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run FastAPI app (Test)
      run: |
        uvicorn main:app --host 0.0.0.0 --port 8000 &
        sleep 5
        curl http://127.0.0.1:8000/docs
```
---
## 📜 License
This project is open-source and available under the **MIT License**.
