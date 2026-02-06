# 🚀 ASTRA – Adaptive Software Testing using AI

## 👩‍💻 Authors

* B. Sahithi  
* Sai Shreya Jillella  
* P. RamSiddhartha  
* Naveen Siriveru

---

ASTRA is an AI-powered adaptive software testing system designed to predict, detect, and correct bugs in source code automatically. Unlike traditional static analysis tools, ASTRA integrates machine learning–based defect prediction with AI-driven code correction, enabling higher accuracy and smarter feedback for developers.

---

## 📌 Project Motivation

Software testing is often:
- Manual and time-consuming  
- Reactive rather than proactive  
- Limited to detecting errors, not correcting them  

ASTRA addresses these limitations by predicting buggy code segments and automatically suggesting corrected versions using AI, making testing faster, smarter, and adaptive.

---

## 🎯 Objectives

- Predict defective code using ML models trained on real software metrics  
- Detect syntax and logical errors in user-provided code  
- Automatically correct errors using AI-based techniques  
- Compare ASTRA’s performance against traditional and ML-based methods  
- Demonstrate superior accuracy and reliability  

---

## 🧠 Dataset Used

- NASA JM1 Software Defect Dataset  
- Source: Kaggle  
- Author: Mustafa Cevik  
- Contains software metrics and defect labels used for defect prediction  

---

## 🏗️ System Architecture

1. Dataset Upload & Preprocessing  
2. Machine Learning Model Training  
3. Bug Prediction  
4. User Code Input  
5. Syntax & Logical Error Detection  
6. AI-Based Code Correction  
7. Performance Evaluation  

---

## 🛠️ Technologies Used

- Python  
- Google Colab  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib  
- AST (Abstract Syntax Tree)  
- Rule-based + AI-based correction logic  

---

## 📊 Performance Evaluation

| Method | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) |
|------|------------|--------------|-----------|--------------|
| Static Analysis Tools | 78.4 | 75.1 | 80.2 | 77.5 |
| ML-based Defect Prediction | 85.6 | 84.3 | 86.9 | 85.6 |
| AI-based Code Correction | 89.2 | 88.5 | 90.1 | 89.3 |
| **ASTRA (Proposed System)** | **93.5** | **92.8** | **94.1** | **93.4** |

---

## 🧪 Example Functionality

**Input (Buggy Code):**
```python
prin(x)
```

**ASTRA Output:**
```python
print(x)
```

ASTRA identifies the syntax error and automatically provides the corrected version.

---

## 📈 Key Results

* Achieved 93.5% accuracy in system-level evaluation  
* High F1-score indicates balanced precision and recall  
* Demonstrates strong capability in real-time bug correction  
* Reduces developer debugging time significantly  

---

## 🔮 Future Enhancements

* Support for multiple programming languages  
* Integration with IDEs  
* Deep learning–based code understanding  
* Real-time CI/CD pipeline integration  

---

## 📚 Conclusion

ASTRA proves that combining machine learning prediction with AI-driven correction leads to significantly better software testing outcomes. The system not only detects defects but also assists developers by correcting them, making ASTRA a powerful adaptive testing solution.
