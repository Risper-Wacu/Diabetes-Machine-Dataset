
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes

#Setup data and loading it
diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target
feature_names = diabetes.feature_names

# Training the model
model = LinearRegression() # create an instance of the linear regression model
model.fit(X, y) # fit the model to the training data

#sidebar for input
with st.sidebar:
    st.header("⚙️ Patient Parameters")
    st.markdown("Enter clinical values below:")
    
    inputs = {}
    #this provides a mix of inputs, Number inputs & Sliders
    for i, col in enumerate(feature_names):
        if col in ['bmi', 'bp', 'age']:
            #using Sliders for bmi, bp and age.
            inputs[col] = st.slider(f"{col.upper()}", -0.2, 0.2, 0.0, 0.01)
        else:
            #using Number Inputs for serum/blood markers
            inputs[col] = st.number_input(f"{col.upper()}", value=0.0, step=0.01)
    
    input_df = pd.DataFrame([inputs])
    
    st.divider()
    if st.button("Reset All Fields", use_container_width=True):
        st.rerun()

#Project Title & Description
st.title("Diabetes Disease Progression Predictor")
st.caption("Strategic Healthcare Analytics | Data-Driven Clinical Support")

st.divider()

#Model Description Section
st.subheader("📋 Model Description")
st.markdown(f"""
This application predicts **diabetes disease progression** one year after baseline 
using a quantitative clinical dataset.

* **Dataset:** Scikit-learn Diabetes Dataset (442 Patients).
* **Target Variable:** A quantitative measure of disease progression one year after baseline.
* **Algorithm:** Ordinary Least Squares (Linear Regression).
* **Purpose:** To provide a predictive baseline for healthcare providers to assess 
    potential patient risk based on ten physiological variables.
""")

st.divider()

#predict
st.subheader("📊 Prediction Analysis")
st.write("Ensure all parameters are set in the sidebar before running the diagnostic.")

if st.button("Generate Diagnostic Report", type="primary", use_container_width=True):
    prediction = model.predict(input_df)[0]
    
    st.metric(label="Estimated Progression Score", value=f"{prediction:.2f}")
    
    #If statements
    if prediction < 100:
        st.success(f"**Low Risk:** The predicted score of {prediction:.2f} is well below the progression threshold.")
    elif 100 <= prediction <= 200:
        st.info(f"**Moderate Risk:** The predicted score of {prediction:.2f} indicates a stable progression pattern.")
    else:
        st.error(f"**High Risk:** The predicted score of {prediction:.2f} indicates a high likelihood of rapid progression.")

st.divider()

#Model use cases
st.subheader("Real-World Applications of the project")
st.markdown("""
How this model can be utilized in a clinical or research setting:
1.  **Clinical Decision Support:** Helping doctors identify high-risk patients who need early intervention.
2.  **Resource Allocation:** Allowing hospitals to prioritize intensive care for patients with high predicted scores.
3.  **Preventative Medicine:** Assisting patients in understanding how changes in metrics (like BMI or BP) might affect their progression score.
4.  **Academic Research:** Serving as a baseline for longitudinal studies on diabetes management.
""")