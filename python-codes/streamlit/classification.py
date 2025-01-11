#import the needed libraries
import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data #store the loaded data into temporary memorey (no need to reload everytime)
#write a function to load the iris data
def load_data():
    iris = load_iris() #load the data
    #convert the input feature data into dataframe
    df = pd.DataFrame(iris.data, columns= iris.feature_names)
    #create a species column which stores the response variable
    df['species'] = iris.target
    #return the whole dataframe (bot x and y) and the output variable names
    return df, iris.target_names


#use the function defined above 
df, target_names = load_data()

#train your model
model = RandomForestClassifier()
model.fit(df.iloc[:,:-1], df['species'])

#create a slider at the sidebar using the minimun and maximum values of the input features
st.title("Input features")
sepal_length = st.sidebar.slider("sepal length", float(df['sepal length (cm)'].min()), float(df["sepal length (cm)"].max()))
sepal_width = st.sidebar.slider("sepal width", float(df['sepal width (cm)'].min()), float(df["sepal width (cm)"].max()))
petal_length = st.sidebar.slider("petal length ", float(df['petal length (cm)'].min()), float(df["petal length (cm)"].max()))
petal_width  = st.sidebar.slider("petal width", float(df['petal width (cm)'].min()), float(df["petal width (cm)"].max()))

#put the input feature silder in 2 dimensional array
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

prediction = model.predict(input_data) #predict
#use the predicted value as index to get the corresponding name
predicted_species = target_names[prediction[0]]

#visulize your output
st.write("Prediction")
st.write(f"Predicted species is : {predicted_species}")