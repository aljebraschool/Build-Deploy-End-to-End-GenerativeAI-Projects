import streamlit as st
import pandas as pd
import numpy as np


#Setting the application title
st.title("Creating my first Application in Strealit")

#display a text
st.write("This is a text")

df = pd.DataFrame({
        "first_column" : [1, 2, 3],
        "second_column" : [5, 7, 8]
        })

#Now Display the dataframe
st.write("Displying the Dataframe...\n")
st.write(df)

#craete a line chat
chat_data = pd.DataFrame(
    np.random.rand(20, 3),
    columns=["a", "b", "c"]
)
st.line_chart(chat_data)