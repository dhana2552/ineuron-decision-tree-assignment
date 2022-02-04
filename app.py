import streamlit as st
import pickle
import pandas as pd

results = pickle.load(open('results.pkl', 'rb'))
predictions = pd.DataFrame(results)


st.title("Decision Tree Classifier Assignment")
st.markdown("This page contains the list of passengers taken as part as test set for Decision Tree Classifier Assignment by iNeuron.ai.  ")
st.image('titanic_image.PNG')

selected_name = st.selectbox(
    "Select a name and click predict to view the prediction result with passenger's details ",
    (predictions['Name'])
)

if st.button('Predict'):
    get_survival_result = predictions[predictions['Name'] == selected_name]
    if get_survival_result['Survived'].values[0] == 1:
        st.header('This person survived as per the prediction')
        st.text("Below are the selected passenger's details")
        st.info(f"Age: {get_survival_result['Age'].values[0]}\
            Ticket Fare:{get_survival_result['Fare'].values[0]}\
            Family Count: {get_survival_result['family_count'].values[0]}\
            Passenger Class: {get_survival_result['Pclass'].values[0]}"
        )
    else:
        st.header('This person did not survive as per the prediction')
        st.text("Below are the selected passenger's details")
        st.info(f"Age: {get_survival_result['Age'].values[0]}\
            Ticket Fare:{get_survival_result['Fare'].values[0]}\
            Family Count: {get_survival_result['family_count'].values[0]}\
            Passenger Class: {get_survival_result['Pclass'].values[0]}"
                )
