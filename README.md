# Academic-Data-Drift-and-Copy-Behavior-Analyzer
# 📊 Academic Data Drift & Copy Behavior Analyzer

## 📌 Overview

This project is part of the **Code2Xplore – 60 Days Challenge (Day-10)** at SRM University–AP.
The goal is to analyze how improper data copying (shallow vs deep copy) can lead to **data drift** and inconsistencies in student academic records.

---

## 🎯 Objective

* Generate student academic data
* Apply shallow and deep copy techniques
* Perform mutations on copied data
* Analyze statistical changes using NumPy & Pandas
* Detect **data drift** and **copy failure**

---

## 🧠 Key Concepts Used

* Python Data Structures (List, Dictionary, Tuple)
* Functions
* NumPy (Mean, Std Deviation)
* Pandas (DataFrame)
* Random Data Generation
* Math Functions
* Shallow Copy vs Deep Copy

---

## 🗂️ Data Format

Each student record:

```json
{
  "id": int,
  "marks": int,
  "attendance": int,
  "scores": [internal, assignment]
}
```

---

## ⚙️ Working Process

### 1. Data Generation

* Generate 10–15 student records using random values

### 2. Copy Creation

* Create:

  * Shallow Copy
  * Deep Copy

### 3. Mutation

Applied ONLY on copied data:

* marks = marks + √marks
* Modify scores list
* Increase attendance

### 4. Analysis

* Mean, Median, Standard Deviation
* Drift Calculation
* Normalization of marks

### 5. Pattern Detection

* Stable Data
* Minor Drift
* Critical Drift
* Copy Failure Detected

---

## 🔍 Personalization Logic

Register Number: **24110011661**

```
24110011661 % 3 = 2
```

➡️ Mutation applied only on indices divisible by **2**
(0, 2, 4, 6, ...)

---

## 📉 Drift Formula

```
drift = |original_mean - modified_mean|
```

---

## ⚠️ Key Insight

### Why does shallow copy cause problems?

Shallow copy does not create a separate copy of nested objects.
The `scores` list is shared between original and copied data.

➡️ When modified in copied data, it also changes original data
➡️ This leads to **Copy Failure**

---

## 📌 Sample Output

* Original DataFrame
* Shallow Copy DataFrame
* Deep Copy DataFrame
* Drift Value
* Tuple → (mean, drift, std_dev)
* Final Classification

---

## 🛠️ Technologies Used

* Python 3
* NumPy
* Pandas

---

## 🚀 How to Run

```bash
pip install numpy pandas
python your_file_name.py
```

---

## 📚 Learning Outcomes

* Understood shallow vs deep copy behavior
* Learned how data drift occurs in real systems
* Applied statistical analysis using NumPy
* Improved understanding of data consistency

---

## 👩‍💻 Author

**Kundana Vadlamudi**
SRM University–AP

---

## 📄 License

This project is for academic purposes only.

