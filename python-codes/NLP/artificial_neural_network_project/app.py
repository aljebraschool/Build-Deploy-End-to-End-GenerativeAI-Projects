import tensorflow as tf
from tensorflow.keras.models import load_model
import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

#load the trained model
model = tf.keras.models.load_model('model.h5')

#load the onehot encoder, label encoder and scaler
with open('onehot_encoder_geography.pkl', 'rb') as file:
    onehot_encoder_geography = pickle.load(file)

with open('label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)


#Streamlit app
st.title("Customer Churn Prediction")

#user input
geography = st.selectbox("Geography", onehot_encoder_geography.categories_[0])
gender = st.selectbox("Gender", label_encoder_gender.classes_)
age = st.slider("Age", min_value=18, max_value= 90)
balance = st.number_input(label = "Balance")
credit_score = st.number_input(label = "Credit Score")
estimated_salary = st.number_input(label = "Estimated Salary")
tenure = st.slider(label = "Tenure", min_value = 0, max_value = 10)
number_of_product = st.slider(label = "Number of Products", min_value=1, max_value=4)
has_credit_card = st.selectbox("Has Credit Card", [0, 1])
is_active_member = st.selectbox("Is Active Member", [0, 1])

#prepare the input data in dataframe dictionary
input_data = pd.DataFrame(
    {
        'CreditScore': [credit_score],
        'Gender' : [label_encoder_gender.transform([gender])[0]],
        'Age': [age],
        'Tenure' : [tenure],
        'Balance' : [balance],
        'NumOfProducts' : [number_of_product],
        'HasCrCard' : [has_credit_card],
        'IsActiveMember' : [is_active_member],
        'EstimatedSalary' : [estimated_salary],
        
    }
)

#now process the geography input
geography_reshaped = np.array([[geography]])

geography_encoded = onehot_encoder_geography.transform(geography_reshaped)

geography_df = pd.DataFrame(geography_encoded, columns=onehot_encoder_geography.get_feature_names_out(['Geography']))

#join this to the input_data dataframe
input_data = pd.concat([input_data, geography_df], axis = 1)

#scale your input data
scaled_input_data = scaler.transform(input_data)

#make prediction
prediction = model.predict(scaled_input_data)

prob_prediction = prediction[0][0]

st.write(f"Churn Probability {prob_prediction:.2f}")

if prob_prediction > 0.5:
    st.write("Customer is likely to churn")
else:
    st.write("customer is not likely to churn")


#This can be used to test your app via the terminal before using streamlit
def main():
    try:
        # Load the trained model
        model = load_model('model.h5')
        print("Model loaded successfully!")

        # Example input data
        example_input = [[25, 7000, 750, 50000, 1]]  # Replace with actual input data

        # Make a prediction
        predictions = model.predict(example_input)
        print("Predictions:", predictions)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()



