# Diabetes Disease Progression Predictor
This is an end-to-end Machine Learning project that predicts disease progression in diabetes patients using physiological markers. This project includes data analysis, visualization of feature interactions, and a deployed web application.
### Check out the interactive web app here: [Diabetes Disease Progression Predictor on Render] (https://diabetes-machine-dataset.onrender.com)
This project utilizes the Scikit-Learn Diabetes dataset (442 samples) to build a Linear Regression model. 

### Key Insights:
* **Strongest Predictors:** BMI (Body Mass Index) and S5 (Serum Triglycerides) were identified as the most significant drivers of disease progression.
* **Feature Interaction:** We discovered a **non-parallel interaction** between BMI and Sex, showing that BMI impacts different demographic groups with varying intensities.
* **Model Performance:** The model achieved an R2 score of 0.45, providing a reliable baseline for clinical "ballpark" estimates.

## Tech Stack
* **Language:** Python 3.12+
* **Libraries:** Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn
* **Deployment:** Streamlit & Render
* **Version Control:** Git & GitHub

## 📁 File Structure
* DIABETES.ipynb: Full Exploratory Data Analysis (EDA) and Model Training.
* Diabetes.py: Streamlit application script for the web interface.
* LinearRegression.pkl: The saved trained model.
* Project Report Diabetes.docx: A detailed 6-page project documentation.
* requirements.txt: List of necessary Python libraries.

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/Risper-Wacu/Diabetes-Machine-Dataset.git](https://github.com/Risper-Wacu/Diabetes-Machine-Dataset.git)
