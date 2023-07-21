import pickle
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import webbrowser

data=pd.read_csv("C:/Shonith/Shonith DS/Modules/Datasets/Final project/streamlit_data.csv")

pickle_in = open("C:/Shonith/Shonith DS/Modules/Datasets/Final project/project1.pkl","rb")
classifier=pickle.load(pickle_in)


def main():
    # Set page title and icon
    st.set_page_config(page_title='Customer Conversion Prediction', layout='wide')

    # App title
    st.title('Customer Conversion Prediction')

    # User Input Details
    st.header('Enter the details to get the prediction')

    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("Select the Age", int(data.age.min()), int(data.age.max()))
        job = st.selectbox("Select the Occupation ", data.job.unique())
        if job == 'blue-collar':
            grouped = data[data['job'] == 'blue-collar']
            job = 0
        elif job == 'entrepreneur':
            grouped = data[data['job'] == 'entrepreneur']
            job = 1
        elif job == 'housemaid':
            grouped = data[data['job'] == 'housemaid']
            job = 2
        elif job == 'services':
            grouped = data[data['job'] == 'services']
            job = 3
        elif job == 'technician':
            grouped = data[data['job'] == 'technician']
            job = 4
        elif job == 'self-employed':
            grouped = data[data['job'] == 'self-employed']
            job = 5
        elif job == 'admin.':
            grouped = data[data['job'] == 'admin.']
            job = 6
        elif job == 'management':
            grouped = data[data['job'] == 'management']
            job = 7
        elif job == 'unemployed':
            grouped = data[data['job'] == 'unemployed']
            job = 8
        elif job == 'retired':
            grouped = data[data['job'] == 'retired']
            job = 9
        elif job == 'student':
            grouped = data[data['job'] == 'student']
            job = 10

        education_qual = st.selectbox("Select the Education qualification ", data.education_qual.unique())
        if education_qual == 'primary':
            grouped = data[data['education_qual'] == 'primary']
            education_qual = 0
        elif education_qual == 'secondary':
            grouped = data[data['education_qual'] == 'secondary']
            education_qual = 1
        elif education_qual == 'tertiary':
            grouped = data[data['education_qual'] == 'tertiary']
            education_qual = 2

        call_type = st.selectbox("Select the Call type ", data.call_type.unique())
        if call_type == 'unknown':
            grouped = data[data['call_type'] == 'unknown']
            call_type = 0
        elif call_type == 'telephone':
            grouped = data[data['call_type'] == 'telephone']
            call_type = 1
        elif call_type == 'cellular':
            grouped = data[data['call_type'] == 'cellular']
            call_type = 2

        day = st.slider("Select the day ", int(data.day.min()), int(data.day.max()))
    with col2:
        dur = st.slider("Select the Call duration ", int(data.dur.min()), int(data.dur.max()))
        mon = st.selectbox("Select the month", data.mon.unique())
        if mon == 'may':
            grouped = data[data['mon'] == 'may']
            mon = 0
        elif mon == 'jul':
            grouped = data[data['mon'] == 'jul']
            mon = 1
        elif mon == 'jan':
            grouped = data[data['mon'] == 'jan']
            mon = 2
        elif mon == 'nov':
            grouped = data[data['mon'] == 'nov']
            mon = 3
        elif mon == 'jun':
            grouped = data[data['mon'] == 'jun']
            mon = 4
        elif mon == 'aug':
            grouped = data[data['mon'] == 'aug']
            mon = 5
        elif mon == 'feb':
            grouped = data[data['mon'] == 'feb']
            mon = 6
        elif mon == 'apr':
            grouped = data[data['mon'] == 'apr']
            mon = 7
        elif mon == 'oct':
            grouped = data[data['mon'] == 'oct']
            mon = 8
        elif mon == 'sep':
            grouped = data[data['mon'] == 'sep']
            mon = 9
        elif mon == 'dec':
            grouped = data[data['mon'] == 'dec']
            mon = 10
        elif mon == 'mar':
            grouped = data[data['mon'] == 'mar']
            mon = 11

        marital = st.selectbox("Select the Marital status ", data.marital.unique())
        if marital == 'divorced':
            grouped = data[data['marital'] == 'marital']
            marital = 1
        elif marital == 'single':
            grouped = data[data['marital'] == 'marital']
            marital = 2
        elif marital == 'married':
            grouped = data[data['marital'] == 'marital']
            marital = 0

        prev_outcome = st.selectbox("Select the Previous Outcome ", data.prev_outcome.unique())
        if prev_outcome == 'failure':
            grouped = data[data['prev_outcome'] == 'prev_outcome']
            prev_outcome = 1
        elif prev_outcome == 'unknown':
                grouped = data[data['prev_outcome'] == 'prev_outcome']
                prev_outcome = 0
        elif prev_outcome == 'other':
                grouped = data[data['prev_outcome'] == 'prev_outcome']
                prev_outcome = 2
        elif prev_outcome == 'success':
                grouped = data[data['prev_outcome'] == 'prev_outcome']
                prev_outcome = 3

        num_calls = st.slider("Select the Number of calls made to customer ", int(data.num_calls.min()),
                              int(data.num_calls.max()))

    input = pd.DataFrame([[age, job, education_qual, call_type, day, mon, dur, num_calls, marital,prev_outcome]])

    if st.button("Predict"):
        valu = classifier.predict(input)
        if valu == 0:
            st.write('DECLINED')
        else:
            col1 = st.columns(1)
            with col1:
                st.write('ACCEPTED')

if __name__=='__main__':
    main()
