# 📊 Customer Churn Prediction with Docker

This project demonstrates an **end-to-end Machine Learning workflow** for predicting customer churn.  
It covers **data preprocessing, model training, evaluation, and deployment inside Docker** for portability and reproducibility.  

---

## 🚀 Project Overview

- **Model Development**  
  - Preprocessed customer behavior data (Telco Churn dataset).  
  - Engineered features and trained a **Random Forest Classifier**.  
  - Achieved ~79% accuracy in predicting customer churn vs. retention.  

- **Deployment with Docker**  
  - Trained model (`model.pkl`) and inference script (`main.py`) packaged inside a **Docker container**.  
  - Uses a lightweight **Python 3.10-slim** base image with dependencies managed via `requirements.txt`.  
  - Anyone can run churn predictions locally with a single `docker build` and `docker run`.  

---

## 🛠️ Tech Stack

- **Programming:** Python  
- **Libraries:** pandas, scikit-learn, joblib  
- **Model:** Random Forest Classifier  
- **Deployment:** Docker (Python 3.10-slim image)  

---

## 📂 Project Structure

```plaintext
customer_churn_pipeline/
├── app/
│   ├── main.py        # Inference script
│   ├── model.pkl      # Trained ML model
│
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker build instructions
├── customer_churn_pipeline.ipynb  # Model training notebook
├── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Dataset (Kaggle)
```
## 🧑‍💻 Author

Apurva Bhoir
This is a personal original project designed, coded, and created by me.
